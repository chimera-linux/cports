pkgname = "avahi2dns"
pkgver = "0.1.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["avahi", "dinit-chimera", "dinit-dbus"]
depends = ["avahi"]
pkgdesc = "DNS server that interfaces with Avahi"
license = "MIT"
url = "https://github.com/LouisBrunner/avahi2dns"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ec2df093342d6fdd324db34a677086b80690e9f91f143a5be7783552c5c598b9"


def post_install(self):
    self.install_service(self.files_path / "avahi2dns")
    self.install_license("LICENSE")
