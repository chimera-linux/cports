pkgname = "musl-mallocng"
pkgver = "1.2.5_git20240622"
pkgrel = 0
_commit = "ab31e9d6a0fa7c5c408856c89df2dfb12c344039"
_scudo_ver = "18.1.8"
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--disable-gcc-wrapper",
    "--with-malloc=mallocng",
]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake"]
depends = [
    f"musl-progs~{pkgver}",
    "base-files",
    "virtual:musl-safety-override!base-files",
]
provides = ["so:libc.so=0"]
provider_priority = 0
replaces = [f"musl~{pkgver}"]
pkgdesc = "Musl C library (with mallocng allocator)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org"
source = [
    f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz",
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{_scudo_ver}/compiler-rt-{_scudo_ver}.src.tar.xz",
]
source_paths = [".", "compiler-rt"]
sha256 = [
    "18c73238e9678e7480de830701925baac0fa6cd0160bf6807b30e949196e538b",
    "e054e99a9c9240720616e927cb52363abbc8b4f1ef0286bad3df79ec8fdf892f",
]
compression = "deflate"
# scp makes it segfault
hardening = ["!scp"]
# does not ship tests
options = ["!check", "!lto"]


def post_extract(self):
    # reported in libc.so --version
    with open(self.cwd / "VERSION", "w") as f:
        f.write(pkgver)
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
    # but also remove musl's x86_64 asm memcpy as it's actually
    # noticeably slower than the c implementation
    self.rm("src/string/x86_64/memcpy.s")


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

    # remove devel stuff provided by main package
    self.uninstall("usr/include")
    self.uninstall("usr/lib/*.o", glob=True)
    for f in (self.destdir / "usr/lib").glob("*.a"):
        if f.name == "libc.a":
            continue
        f.unlink()


@subpackage("musl-mallocng-devel-static")
def _static(self):
    self.depends = [f"musl-devel~{pkgver}"]

    return ["usr/lib/libc.a"]
