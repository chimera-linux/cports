pkgname = "libdisplay-info"
pkgver = "0.3.0"
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
sha256 = "2b467e3336aec63819d6aca28d7310d3dc7415b2b3a3c3a5aec9d3727053c078"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdisplay-info-devel")
def _(self):
    return self.default_devel()
