pkgname = "hyprland-protocols"
pkgver = "0.7.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Wayland protocol extensions for Hyprland"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprland-protocols"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ee419006d7cd20927b9b7c8b5fc430571c151b0385d600508de1a7957294498c"

options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
