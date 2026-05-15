pkgname = "listenbrainz-mpd"
pkgver = "2.5.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel"]
pkgdesc = "ListenBrainz submission client for MPD"
license = "AGPL-3.0-only"
url = "https://codeberg.org/elomatreb/listenbrainz-mpd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1b2b586459e0b3720ca87aaf2bcaaa67c9bc28f7997d6798a2e0c7d4e51fdbbc"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/listenbrainz-mpd"
    )
    self.install_license("LICENSE.txt")
