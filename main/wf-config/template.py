pkgname = "wf-config"
pkgver = "0.10.0"
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
sha256 = "9676f08248aaf83b91ecce5c953326c4341084b6efa00d3757a936617a51e487"
# vis breaks syumbols
hardening = ["!vis"]
# missing doctest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wf-config-devel")
def _(self):
    return self.default_devel()
