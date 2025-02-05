pkgname = "listenbrainz-mpd"
pkgver = "2.3.8"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel"]
pkgdesc = "ListenBrainz submission client for MPD"
maintainer = "JetpackJackson <jetpackjackson@katzenmue.de>"
license = "AGPL-3.0-only"
url = "https://codeberg.org/elomatreb/listenbrainz-mpd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0a3456029c6eb73b391b1ad3b0f01795554c3b040f63998112a4a5fe8cbc7637"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/listenbrainz-mpd"
    )
    self.install_license("LICENSE.txt")
