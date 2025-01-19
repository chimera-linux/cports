pkgname = "dialog"
pkgver = "1.3.20250116"
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
source = f"https://invisible-mirror.net/archives/dialog/dialog-{pkgver.replace('.2025', '-2025')}.tgz"
sha256 = "68406329827b783d0a8959cc20a94c6e1791ac861a27f854e06e9020541816dd"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/lib")
