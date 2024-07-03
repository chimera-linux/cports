pkgname = "dialog"
pkgver = "1.3.20240619"
pkgrel = 0
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
sha256 = "5d8c4318963db3fd383525340276e0e05ee3dea9a6686c20779f5433b199547d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/lib")
