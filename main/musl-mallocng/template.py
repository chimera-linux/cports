pkgname = "musl-mallocng"
pkgver = "1.2.5"
pkgrel = 0
_commit = "v1.2.5"
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
source = f"https://git.musl-libc.org/cgit/musl/snapshot/musl-{_commit}.tar.gz"
sha256 = "5829457efb2247c1e39920b14721b75e9c488a06149736c8317536ec4aa3764b"
# scp makes it segfault
hardening = ["!scp"]
# does not ship tests
options = ["!check", "!lto"]


def pre_install(self):
    self.install_dir("usr/lib")
    # ensure all files go in /usr/lib
    self.install_link("usr/lib", "lib")

    self.install_license("COPYRIGHT")


def post_install(self):
    # no need for the symlink anymore
    self.rm(self.destdir / "lib")

    # fix up ld-musl-whatever so it does not point to absolute path
    for f in (self.destdir / "usr/lib").glob("ld-musl-*.so.1"):
        f.unlink()
        f.symlink_to("libc.so")

    # remove devel stuff provided by main package
    self.rm(self.destdir / "usr/include", recursive=True)
    for f in (self.destdir / "usr/lib").glob("*.o"):
        f.unlink()
    for f in (self.destdir / "usr/lib").glob("*.a"):
        if f.name == "libc.a":
            continue
        f.unlink()


@subpackage("musl-mallocng-devel-static")
def _static(self):
    self.depends = [f"musl-devel~{pkgver}"]

    return ["usr/lib/libc.a"]
