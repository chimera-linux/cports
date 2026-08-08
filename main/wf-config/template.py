pkgname = "wf-config"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "glm",
    "libevdev-devel",
    "libxml2-devel",
    "linux-headers",
]
pkgdesc = "Library for managing configuration files written for Wayfire"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wf-config/releases/download/v{pkgver}/wf-config-{pkgver}.tar.xz"
sha256 = "b7721326ade8d42b25ecd2d572e5deb853b1327672608472854c6473bc8d2514"
# vis breaks syumbols
hardening = ["!vis"]
# missing doctest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wf-config-devel")
def _(self):
    return self.default_devel()
