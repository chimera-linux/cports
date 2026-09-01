pkgname = "hyprutils"
pkgver = "0.14.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "pixman-devel",
]
pkgdesc = "Hyprland utilities library"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprutils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e8cfb093d8124de1e63d3635b7d749758d0919c2e1b3ce44462ef7ab003060c4"

# tests are disabled for release builds upstream
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("hyprutils-devel")
def _(self):
    return self.default_devel()
