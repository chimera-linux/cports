pkgname = "libspng"
pkgver = "0.7.4"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
provides = [self.with_pkgver("spng")]
replaces = ["spng<0.7.5"]
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


@subpackage("libspng-devel")
def _(self):
    self.provides = [self.with_pkgver("spng-devel")]
    self.replaces = ["spng-devel<0.7.5"]
    return self.default_devel()
