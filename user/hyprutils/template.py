pkgname = "hyprutils"
pkgver = "0.13.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "clang",
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["pixman-devel"]
pkgdesc = "Hypr ecosystem utilities"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprutils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "480ee026105deea64a24eb96d80cabe54b357594ce36cb05c021ea226c69aede"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("hyprutils-devel")
def _(self):
    return self.default_devel()
