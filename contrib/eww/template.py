pkgname = "eww"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["gtk-layer-shell-devel", "rust-std"]
pkgdesc = "Standalone widget system for wayland written in rust"
maintainer = "Nova <froggo8311@proton.me>"
license = "MIT"
url = "https://elkowar.github.io/eww"
source = f"https://github.com/elkowar/eww/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ea4f62e48e3750a361e0f359933d7d840d158592ff5b3683ba1f3ccf42bda819"


def do_install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/eww")
    self.install_license("LICENSE")
