pkgname = "iwgtk"
pkgver = "0.9"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "gtk4-devel",
    "qrencode-devel",
]
pkgdesc = "Graphical frontend for iwd"
license = "GPL-3.0-or-later"
url = "https://github.com/J-Lentz/iwgtk"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "84a82dc730fe536034a65d148840e975c1353f4114db527439170ff410583d31"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_service(self.files_path / "iwgtk.user")
