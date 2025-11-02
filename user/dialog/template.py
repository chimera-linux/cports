pkgname = "dialog"
pkgver = "1.3.20251001"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
# broken to reconf
configure_gen = []
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/dialog/dialog-{pkgver.replace('.2025', '-2025')}.tgz"
sha256 = "bee47347a983312facc4dbcccd7fcc86608d684e1f119d9049c4692213db96c3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/lib")
