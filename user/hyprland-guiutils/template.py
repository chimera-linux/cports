pkgname = "hyprland-guiutils"
pkgver = "0.2.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "aquamarine-devel",
    "cairo-devel",
    "hyprgraphics-devel",
    "hyprlang-devel",
    "hyprtoolkit-devel",
    "hyprutils-devel",
    "libdrm-devel",
    "libxkbcommon-devel",
    "pixman-devel",
]
pkgdesc = "Hyprland GUI utilities"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprland-guiutils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "16f92a6c5a22ac58e1fc313f6b202c188da45e804e1f21ff57dfd0da5c1a01b7"


def post_install(self):
    self.install_license("LICENSE")
