pkgname = "wf-config"
pkgver = "0.7.1"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wf-config/releases/download/v{pkgver}/wf-config-{pkgver}.tar.xz"
sha256 = "7d2285adeaca0ff6e36e6ef450564ab02c8e26ba5da3b169257c5bf061f7e5f0"
# vis breaks syumbols
hardening = ["!vis"]
# missing doctest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wf-config-devel")
def _devel(self):
    return self.default_devel()
