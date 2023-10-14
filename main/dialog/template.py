pkgname = "dialog"
pkgver = "1.3.20231002"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/{pkgname}/{pkgname}-{pkgver.replace('.2023', '-2023')}.tgz"
sha256 = "315640ab0719225d5cbcab130585c05f0791fcf073072a5fe9479969aa2b833b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib", force=True, recursive=True)


configure_gen = []
