pkgname = "musl"
pkgver = "1.2.6"
pkgrel = 5
_commit = "9fa28ece75d8a2191de7c5bb53bed224c5947417"
_mimalloc_ver = "2.2.7"
build_style = "gnu_configure"
_configure_base = ["--prefix=/usr", "--disable-gcc-wrapper"]
configure_args = [*_configure_base]
configure_gen = []
make_build_args = []
depends = [self.with_pkgver("musl-ldso"), self.with_pkgver("musl-progs")]
provides = ["so:libc.so=0"]
provider_priority = 999
replaces = []
pkgdesc = "Musl C library"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz",
    f"https://github.com/microsoft/mimalloc/archive/refs/tags/v{_mimalloc_ver}.tar.gz",
]
source_paths = [".", "mimalloc"]
sha256 = [
    "d3baf222d234f2121e71b7eabd0c17667b7a3733b3077e99f9920c69cb5899df",
    "8e0ed89907a681276bff2e49e9a048b47ba51254ab60daf6b3c220acac456a95",
]
tool_flags = {"CFLAGS": []}
compression = "deflate"
# scp makes it segfault
hardening = ["!scp"]
# does not ship tests
options = ["bootstrap", "!check", "!lto"]

# whether to use musl's stock allocator
# for now 32-bit targets until we patch out 64-bit atomics in arena
_use_mng = self.profile.wordsize == 32

_variant_mng = False
_variant_nvidia = False

if _use_mng:
    configure_args += ["--with-malloc=mallocng"]
else:
    if self.stage >= 2:
        if self.profile.arch in ["aarch64", "x86_64"]:
            _variant_nvidia = True
        _variant_mng = True
    configure_args += ["--with-malloc=external"]

if _variant_mng:
    replaces += [self.with_pkgver("musl-mallocng")]
if _variant_nvidia:
    replaces += [self.with_pkgver("musl-nvidia")]

if self.stage > 0:
    # have base-files extract first in normal installations
    #
    # don't do this for stage 0 though, because otherwise base-files will
    # get installed as a makedepend and subsequently removed as an autodep,
    # which will nuke the base symlinks handled by initial initdb, as the
    # stage0 bldroot is not a complete chroot and relies on the external
    # state we give it during first setup
    #
    # but this only really matters for "real" systems, so in stage 0 we can
    # just avoid the dependency and work around the whole issue
    #
    depends += ["base-files"]


def post_extract(self):
    # reported in libc.so --version
    with open(self.cwd / "VERSION", "w") as f:
        f.write(pkgver)
    # copy in our mimalloc unified source
    self.cp(self.files_path / "mimalloc-verify-syms.sh", ".")
    self.cp(self.files_path / "mimalloc.c", "mimalloc/src")
    # now we're ready to get patched
    # but also remove musl's x86_64 asm memcpy as it's actually
    # noticeably slower than the c implementation
    self.rm("src/string/x86_64/memcpy.s")
    self.rm("src/string/x86_64/memmove.s")


def init_configure(self):
    # ensure that even early musl uses compiler-rt
    if self.stage == 0:
        self.env["LIBCC_LDFLAGS"] = "--rtlib=compiler-rt"
        return


def post_configure(self):
    from cbuild.util import gnu_configure

    if _variant_mng:
        gnu_configure.configure(
            self,
            configure_args=[*_configure_base, "--with-malloc=mallocng"],
            build_dir="build-mng",
        )

    if _variant_nvidia:
        _cflags = list(self.tool_flags["CFLAGS"])
        self.tool_flags["CFLAGS"] += ["-DLIBC_NVIDIA_BUILD"]
        gnu_configure.configure(
            self,
            configure_args=[*_configure_base, "--disable-static"],
            build_dir="build-nv",
        )
        self.tool_flags["CFLAGS"] = _cflags


def build(self):
    from cbuild.util import compiler

    _mi_args = [
        "MALLOC_DIR=external",
        "EXTRA_OBJ=$(srcdir)/src/malloc/external/mimalloc.o",
    ]

    if _use_mng:
        self.make.build()
    else:
        self.make.build(_mi_args)

    if _variant_mng:
        self.make.build(wrksrc="build-mng")

    if _variant_nvidia:
        self.make.build(_mi_args, wrksrc="build-nv")

    self.cp(self.files_path / "getent.c", ".")
    self.cp(self.files_path / "getconf.c", ".")
    self.cp(self.files_path / "iconv.c", ".")
    self.cp(self.files_path / "__stack_chk_fail_local.c", ".")

    cc = compiler.C(self)

    cc.invoke(["getent.c"], "getent")
    cc.invoke(["getconf.c"], "getconf")
    cc.invoke(["iconv.c"], "iconv")

    cc.invoke(
        ["__stack_chk_fail_local.c"],
        "__stack_chk_fail_local.o",
        obj_file=True,
    )
    self.do(
        self.get_tool("AR"),
        "r",
        "libssp_nonshared.a",
        "__stack_chk_fail_local.o",
    )


def pre_install(self):
    self.install_dir("usr/lib")
    # ensure all files go in /usr/lib
    self.install_link("lib", "usr/lib")

    self.install_license("COPYRIGHT")


def post_install(self):
    # no need for the symlink anymore
    self.uninstall("lib")

    # install variants
    if _variant_mng:
        self.install_file(
            "build-mng/lib/libc.so", "usr/lib", mode=0o755, name="libc-mng.so"
        )
        self.install_file(
            "build-mng/lib/libc.a", "usr/lib", mode=0o644, name="libc-mng.a"
        )

    if _variant_nvidia:
        self.install_file(
            "build-nv/lib/libc.so", "usr/lib", mode=0o755, name="libc-nv.so"
        )

    # fix up ld-musl-whatever so it does not point to absolute path
    for f in (self.destdir / "usr/lib").glob("ld-musl-*.so.1"):
        f.unlink()
        f.symlink_to("libc.so")

    self.install_dir("usr/bin")
    self.install_link("usr/bin/ldd", "../lib/libc.so")

    self.install_bin("iconv")
    self.install_bin("getent")
    self.install_bin("getconf")

    self.install_file("libssp_nonshared.a", "usr/lib")

    self.install_man(self.files_path / "getent.1")
    self.install_man(self.files_path / "getconf.1")

    self.install_link("usr/bin/ldconfig", "true")


@subpackage("musl-ldso")
def _(self):
    self.subdesc = "dynamic linker"
    # should work with any variant
    self.options = ["brokenlinks", "!scanrundeps"]
    self.depends = ["so:libc.so!musl"]
    return ["usr/lib/ld-musl-*.so.1"]


@subpackage("musl-progs")
def _(self):
    # we can't have a versioned symlink dep on musl
    self.options = ["brokenlinks", "!scanrundeps"]
    self.depends = ["so:libc.so!musl"]
    return self.default_progs()


@subpackage("musl-devel-static")
def _(self):
    return ["usr/lib/libc.a"]


@subpackage("musl-libssp-static")
def _(self):
    self.subdesc = "libssp_nonshared for some targets"
    self.depends = []

    return ["usr/lib/libssp_nonshared.a"]


@subpackage("musl-mallocng", _variant_mng)
def _(self):
    self.subdesc = "malloc-ng allocator"
    self.depends = [
        "base-files",
        self.with_pkgver("musl-ldso"),
        self.with_pkgver("musl-progs"),
        "virtual:musl-safety-override!base-files",
    ]
    self.provides = ["so:libc.so=0"]
    self.provider_priority = 0
    self.replaces = [self.with_pkgver("musl")]
    if _variant_nvidia:
        self.replaces += [self.with_pkgver("musl-nvidia")]

    def _take():
        self.take("usr/lib/libc-mng.so")
        self.mv(
            self.destdir / "usr/lib/libc-mng.so",
            self.destdir / "usr/lib/libc.so",
        )

    return _take


@subpackage("musl-mallocng-devel-static", _variant_mng)
def _(self):
    self.subdesc = "static libraries for malloc-ng allocator"
    self.depends = [self.with_pkgver("musl-devel")]

    def _take():
        self.take("usr/lib/libc-mng.a")
        self.mv(
            self.destdir / "usr/lib/libc-mng.a", self.destdir / "usr/lib/libc.a"
        )

    return _take


@subpackage("musl-nvidia", _variant_nvidia)
def _(self):
    self.subdesc = "NVIDIA hacks"
    self.depends = [
        "base-files",
        self.with_pkgver("musl-ldso"),
        self.with_pkgver("musl-progs"),
    ]
    self.provides = ["so:libc.so=0"]
    self.provider_priority = 0
    self.replaces = [self.with_pkgver("musl")]
    if _variant_mng:
        self.replaces += [self.with_pkgver("musl-mallocng")]

    def _take():
        self.take("usr/lib/libc-nv.so")
        self.mv(
            self.destdir / "usr/lib/libc-nv.so",
            self.destdir / "usr/lib/libc.so",
        )

    return _take


@subpackage("musl-devel")
def _(self):
    # empty depends so libc.so can be switched with alternatives
    # the libc itself installs as a solib dep of everything anyway
    self.depends = []
    self.options = ["!splitstatic"]
    # the .a files are empty archives
    return ["usr/include", "usr/lib/*.o", "usr/lib/*.a"]
