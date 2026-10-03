pkgname = "libdisplay-info"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "hwdata-devel",
]
pkgdesc = "EDID and DisplayID library"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/libdisplay-info"
source = f"{url}/-/archive/{pkgver}/libdisplay-info-{pkgver}.tar.gz"
sha256 = "787b58aec473830b0030251ba2b880560b4b3853dc5d6961a6e9701abae29b55"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdisplay-info-devel")
def _(self):
    return self.default_devel()
