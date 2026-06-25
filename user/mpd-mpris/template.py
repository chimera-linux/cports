pkgname = "mpd-mpris"
pkgver = "0.4.3"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/mpd-mpris"]
hostmakedepends = ["dinit-chimera", "go", "mpd"]
depends = ["mpd"]
pkgdesc = "MPRIS protocol implementation for MPD"
license = "MIT"
url = "https://github.com/natsukagami/mpd-mpris"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c8737299e6368b15635481508a8dc69448e442e550f7c3123e38f32431a1ae30"


def install(self):
    self.install_bin(f"build/{pkgname}")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "mpd-mpris.user")
