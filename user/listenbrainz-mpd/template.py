pkgname = "listenbrainz-mpd"
pkgver = "2.6.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel"]
pkgdesc = "ListenBrainz submission client for MPD"
license = "AGPL-3.0-only"
url = "https://codeberg.org/elomatreb/listenbrainz-mpd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4d93ff68bb2f53093561d701594f1e53fa3a4409d540f5f2247e98c9ef1b276b"
# no tests
options = ["!check"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/listenbrainz-mpd"
    )
    self.install_license("LICENSE.txt")
