pkgname = "hyprwire"
pkgver = "0.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    f"-DVERSION={pkgver}",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "hyprutils-devel",
    "libffi8-devel",
    "pugixml-devel",
]
pkgdesc = "Fast and consistent wire protocol for IPC"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprwire"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "92a673d40ae6a7d66fbcd0a34ec071e026e17eaeeb0040c3375e4b2a80dba737"

# upstream disables tests for release builds
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("hyprwire-devel")
def _(self):
    return self.default_devel()
