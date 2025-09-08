pkgname = "collada-dom"
pkgver = "2.5.0"
pkgrel = 6
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DBUILD_SHARED_LIBS=ON",
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "libxml2-devel",
    "minizip-devel",
    "uriparser-devel",
]
pkgdesc = "COLLADA DOM access library"
license = "MIT"
url = "https://sourceforge.net/projects/collada-dom"
source = f"https://github.com/rdiankov/collada-dom/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3be672407a7aef60b64ce4b39704b32816b0b28f61ebffd4fbd02c8012901e0d"


def post_install(self):
    self.install_license("licenses/dom_license_e.txt")


@subpackage("collada-dom-devel")
def _(self):
    self.depends += ["boost-devel"]
    return self.default_devel()
