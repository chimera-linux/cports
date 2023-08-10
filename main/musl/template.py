pkgname = "musl"
pkgver = "1.2.4"
pkgrel = 1
_scudo_ver = "16.0.6"
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake"]
provides = ["so:libc.so=0"]
pkgdesc = "Musl C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"http://www.musl-libc.org/releases/{pkgname}-{pkgver}.tar.gz",
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{_scudo_ver}/compiler-rt-{_scudo_ver}.src.tar.xz",
]
source_paths = [".", "compiler-rt"]
sha256 = [
    "7a35eae33d5372a7c0da1188de798726f68825513b7ae3ebe97aaaa52114f039",
    "7911a2a9cca10393a17f637c01a6f5555b0a38f64ff47dc9168413a4190bc2db",
]
# scp makes it segfault
hardening = ["!scp"]
# does not ship tests + allow "broken" symlinks to true
options = ["bootstrap", "!check", "!lto", "brokenlinks"]

# whether to use musl's stock allocator instead of scudo
_use_mng = self.profile().arch in ["ppc"]

if _use_mng:
    configure_args += ["--with-malloc=mallocng"]
elif self.profile().arch == "aarch64":
    # disable aarch64 memory tagging in scudo, as it fucks up qemu-user
    tool_flags = {"CXXFLAGS": ["-DSCUDO_DISABLE_TBI"]}

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
    depends = ["base-files"]


def post_extract(self):
    # prepare scudo subdir
    self.mkdir("src/malloc/scudo/scudo", parents=True)
    # move compiler-rt stuff in there
    scpath = self.cwd / "compiler-rt/lib/scudo/standalone"
    for f in scpath.glob("*.cpp"):
        self.cp(f, "src/malloc/scudo")
    for f in scpath.glob("*.h"):
        self.cp(f, "src/malloc/scudo")
    for f in scpath.glob("*.inc"):
        self.cp(f, "src/malloc/scudo")
    self.cp(scpath / "include/scudo/interface.h", "src/malloc/scudo/scudo")
    # remove wrappers
    for f in (self.cwd / "src/malloc/scudo").glob("wrappers_*"):
        f.unlink()
    # copy in our own wrappers
    self.cp(self.files_path / "wrappers.cpp", "src/malloc/scudo")
    # now we're ready to get patched


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


def do_install(self):
    self.install_dir("usr/lib")
    # ensure all files go in /usr/lib
    self.install_link("usr/lib", "lib")

    self.make.install()

    # no need for the symlink anymore
    self.rm(self.destdir / "lib")

    # fix up ld-musl-whatever so it does not point to absolute path
    for f in (self.destdir / "usr/lib").glob("ld-musl-*.so.1"):
        f.unlink()
        f.symlink_to("libc.so")

    self.install_dir("usr/bin")
    self.install_link("../lib/libc.so", "usr/bin/ldd")

    self.install_bin("iconv")
    self.install_bin("getent")
    self.install_bin("getconf")

    self.install_man(self.files_path / "getent.1")
    self.install_man(self.files_path / "getconf.1")

    self.install_link("true", "usr/bin/ldconfig")


@subpackage("musl-devel-static")
def _static(self):
    return ["usr/lib/libc.a"]


@subpackage("musl-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.options = ["!splitstatic"]
    # the .a files are empty archives
    return ["usr/include", "usr/lib/*.o", "usr/lib/*.a"]
