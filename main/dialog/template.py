pkgname = "dialog"
pkgver = "1.3.20240307"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
# broken to reconf
configure_gen = []
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/{pkgname}/{pkgname}-{pkgver.replace('.2024', '-2024')}.tgz"
sha256 = "339d311c6abb240213426b99ad63565cbcb3e8641ef1989c033e945b754d34ef"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib", force=True, recursive=True)
