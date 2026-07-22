pkgname = "anyrun"
pkgver = "26.6.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "gtk4-layer-shell-devel",
    "pango-devel",
]
depends = ["anyrun-provider"]
pkgdesc = "Customizable runner program for Wayland"
license = "GPL-3.0-or-later"
url = "https://github.com/anyrun-org/anyrun"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0b2abc1da9fdea12a753ca3024d5ede62209b82837d49eb5da35d99ba22a5790"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/anyrun")

    # PLUGIN_PATHS in anyrun-provider
    self.install_file(
        f"target/{self.profile().triplet}/release/*.so",
        "usr/lib/anyrun",
        glob=True,
    )

    # configure this for yourself in ~/.config
    self.install_file("examples/config.ron", "usr/share/examples/anyrun")
