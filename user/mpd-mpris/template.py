pkgname = "mpd-mpris"
pkgver = "0.4.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/mpd-mpris"]
hostmakedepends = [
    "dinit-chimera",
    "go",
    "mpd"
]
depends = ["mpd"]
pkgdesc = "MPRIS protocol implementation for MPD"
license = "MIT"
url = "https://github.com/natsukagami/mpd-mpris"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4167700ee27dfe8ef0a97502b429e3ec25be1161ea00598499720b2e16c0937f"


def install(self):
    self.install_bin(f"build/{pkgname}")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "mpd-mpris.user")
