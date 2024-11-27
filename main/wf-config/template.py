pkgname = "wf-config"
pkgver = "0.9.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wf-config/releases/download/v{pkgver}/wf-config-{pkgver}.tar.xz"
sha256 = "f681fe028aa9026e0c6894d7b94c544230b8285078f176076a3d964fd1dfc37b"
# vis breaks syumbols
hardening = ["!vis"]
# missing doctest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wf-config-devel")
def _(self):
    return self.default_devel()
