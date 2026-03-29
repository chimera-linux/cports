pkgname = "listenbrainz-mpd"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel"]
pkgdesc = "ListenBrainz submission client for MPD"
license = "AGPL-3.0-only"
url = "https://codeberg.org/elomatreb/listenbrainz-mpd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d4f7f157ac40a5e6b4950a3abfda386292861ffea78575b7df86e92826100e22"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/listenbrainz-mpd"
    )
    self.install_license("LICENSE.txt")
