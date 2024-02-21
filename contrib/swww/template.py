pkgname = "swww"
pkgver = "0.8.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Solution to your Wayland Wallpaper Woes"
maintainer = "Nova <froggo8311@proton.me>"
license = "GPL-3.0-only"
url = "https://github.com/LGFae/swww"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6733cda771a0e635dbd00f7aef78ed60f1ccdf640647ecfe02d0cdfdef996b68"


def post_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/swww-daemon")
