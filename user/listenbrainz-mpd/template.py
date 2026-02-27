pkgname = "listenbrainz-mpd"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel"]
pkgdesc = "ListenBrainz submission client for MPD"
license = "AGPL-3.0-only"
url = "https://codeberg.org/elomatreb/listenbrainz-mpd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f08940dbca01009be229828dc904e924245f59598f9f92870c1e8f95493cf63a"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/listenbrainz-mpd"
    )
    self.install_license("LICENSE.txt")
