pkgname = "iwgtk"
pkgver = "0.9"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "qrencode-devel",
    "scdoc",
]
pkgdesc = "Graphical wifi management utility for iwd"
license = "GPL-3.0-or-later"
url = "https://github.com/J-Lentz/iwgtk"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "84a82dc730fe536034a65d148840e975c1353f4114db527439170ff410583d31"


def post_install(self):
    self.uninstall("usr/lib/systemd")
