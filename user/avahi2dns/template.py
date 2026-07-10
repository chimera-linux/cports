pkgname = "avahi2dns"
pkgver = "0.2.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["avahi", "dinit-chimera", "dinit-dbus"]
depends = ["avahi"]
pkgdesc = "DNS server that interfaces with Avahi"
license = "MIT"
url = "https://github.com/LouisBrunner/avahi2dns"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5eb587f4069b097b7a9029258e627154583dc500a51e33d25ccdf1cac37df53f"


def post_install(self):
    self.install_service(self.files_path / "avahi2dns")
    self.install_license("LICENSE")
