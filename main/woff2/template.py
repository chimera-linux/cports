pkgname = "woff2"
pkgver = "1.0.2"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["brotli-devel"]
pkgdesc = "Web Open Font Format 2 reference implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/google/woff2"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "add272bb09e6384a4833ffca4896350fdb16e0ca22df68c0384773c67a175594"
# no test target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("woff2-libs")
def _(self):
    # transitional
    self.provides = [
        self.with_pkgver("libwoff2common"),
        self.with_pkgver("libwoff2dec"),
        self.with_pkgver("libwoff2enc"),
    ]
    return self.default_libs()


@subpackage("woff2-devel")
def _(self):
    return self.default_devel()
