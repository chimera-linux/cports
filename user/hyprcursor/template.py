pkgname = "hyprcursor"
pkgver = "0.1.13"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "clang",
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "hyprlang-devel",
    "librsvg-devel",
    "libzip-devel",
    "tomlplusplus-devel",
]
pkgdesc = "Hyprland cursor format"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprcursor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "82af8b2ce27242ffdd6baebaa71b3f6c8665dc25c52bfcfccc16912622896af8"
# Any cursor theme required for test, but it unreachable
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("hyprcursor-devel")
def _(self):
    return self.default_devel()
