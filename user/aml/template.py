pkgname = "aml"
pkgver = "0.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["musl-bsd-headers"]
pkgdesc = "Main loop library"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://github.com/any1/aml"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cba1ca1689d4031faf37bb7a184559106b6d2f462ae8890a9fa16e3022ca1eb0"


def post_install(self):
    self.install_license("COPYING")


@subpackage("aml-devel")
def _(self):
    return self.default_devel()
