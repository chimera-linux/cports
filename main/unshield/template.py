pkgname = "unshield"
pkgver = "1.6.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Utility for InstallShield CAB archive extraction"
license = "MIT"
url = "https://github.com/twogood/unshield"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a937ef596ad94d16e7ed2c8553ad7be305798dcdcfd65ae60210b1e54ab51a2f"
# runner not integrated
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("unshield-libs")
def _(self):
    return self.default_libs()


@subpackage("unshield-devel")
def _(self):
    return self.default_devel()
