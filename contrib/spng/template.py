pkgname = "spng"
pkgver = "0.7.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Simple PNG library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-2-Clause"
url = "https://libspng.org"
source = (
    f"https://github.com/randy408/libspng/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "47ec02be6c0a6323044600a9221b049f63e1953faf816903e7383d4dc4234487"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("spng-devel")
def _devel(self):
    return self.default_devel()
