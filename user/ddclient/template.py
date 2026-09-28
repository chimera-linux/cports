pkgname = "ddclient"
pkgver = "4.0.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "curl",
]
makedepends = ["dinit-chimera"]
depends = [
    "curl",
    "perl",
]
pkgdesc = "Client used to update dynamic DNS entries"
license = "GPL-2.0-or-later"
url = "https://ddclient.net"
source = (
    f"https://github.com/ddclient/ddclient/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "4b37c99ac0011102d7db62f1ece7ff899b06df3d4b172e312703931a3c593c93"


def post_install(self):
    self.install_service(self.files_path / "ddclient")
    self.install_file("build/ddclient.conf", "usr/share/examples/ddclient")
    self.uninstall("etc/ddclient")
