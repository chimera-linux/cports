pkgname = "musl"
pkgver = "1.2.5_git20240705"
pkgrel = 1
_commit = "dd1e63c3638d5f9afb857fccf6ce1415ca5f1b8b"
_mimalloc_ver = "2.1.7"
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
configure_gen = []
make_cmd = "gmake"
make_build_args = []
hostmakedepends = ["gmake"]
depends = [self.with_pkgver("musl-progs")]
provides = ["so:libc.so=0"]
provider_priority = 999
replaces = [f"musl-mallocng~{pkgver}"]
pkgdesc = "Musl C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz",
    f"https://github.com/microsoft/mimalloc/archive/refs/tags/v{_mimalloc_ver}.tar.gz",
]
source_paths = [".", "mimalloc"]
sha256 = [
    "a6886a65387d2547aae10c1ba31a35529a5c4bbe4205b2a9255c774d5da77329",
    "0eed39319f139afde8515010ff59baf24de9e47ea316a315398e8027d198202d",
]
compression = "deflate"
# scp makes it segfault
hardening = ["!scp"]
# does not ship tests
options = ["bootstrap", "!check", "!lto"]

# whether to use musl's stock allocator
# for now 32-bit targets until we patch out 64-bit atomics in arena
_use_mng = self.profile().wordsize == 32

if _use_mng:
    configure_args += ["--with-malloc=mallocng"]
else:
    configure_args += ["--with-malloc=external"]
    make_build_args += ["EXTRA_OBJ=$(srcdir)/src/malloc/external/mimalloc.o"]

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


def init_configure(self):
    # ensure that even early musl uses compiler-rt
    if self.stage == 0:
        self.env["LIBCC_LDFLAGS"] = "--rtlib=compiler-rt"
        return


def post_build(self):
    from cbuild.util import compiler

    self.cp(self.files_path / "getent.c", ".")
    self.cp(self.files_path / "getconf.c", ".")
    self.cp(self.files_path / "iconv.c", ".")

    cc = compiler.C(self)
    cc.invoke(["getent.c"], "getent")
    cc.invoke(["getconf.c"], "getconf")
    cc.invoke(["iconv.c"], "iconv")


def pre_install(self):
    self.install_dir("usr/lib")
    # ensure all files go in /usr/lib
    self.install_link("lib", "usr/lib")

    self.install_license("COPYRIGHT")


def post_install(self):
    # no need for the symlink anymore
    self.uninstall("lib")

    # fix up ld-musl-whatever so it does not point to absolute path
    for f in (self.destdir / "usr/lib").glob("ld-musl-*.so.1"):
        f.unlink()
        f.symlink_to("libc.so")

    self.install_dir("usr/bin")
    self.install_link("usr/bin/ldd", "../lib/libc.so")

    self.install_bin("iconv")
    self.install_bin("getent")
    self.install_bin("getconf")

    self.install_man(self.files_path / "getent.1")
    self.install_man(self.files_path / "getconf.1")

    self.install_link("usr/bin/ldconfig", "true")


@subpackage("musl-progs")
def _progs(self):
    # we can't have a versioned symlink dep on musl
    self.options = ["brokenlinks", "!scanrundeps"]
    self.depends = ["so:libc.so!musl"]
    return self.default_progs()


@subpackage("musl-devel-static")
def _static(self):
    return ["usr/lib/libc.a"]


@subpackage("musl-devel")
def _devel(self):
    # empty depends so libc.so can be switched with alternatives
    # the libc itself installs as a solib dep of everything anyway
    self.depends = []
    self.options = ["!splitstatic"]
    # the .a files are empty archives
    return ["usr/include", "usr/lib/*.o", "usr/lib/*.a"]
