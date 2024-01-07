pkgname = "wf-config"
pkgver = "0.8.0"
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
sha256 = "16988f63fd054b446d4feac024aafd4cc962193d6d6dfde90e6d6169c23443af"
# vis breaks syumbols
hardening = ["!vis"]
# missing doctest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wf-config-devel")
def _devel(self):
    return self.default_devel()
