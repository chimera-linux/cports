pkgname = "aml"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["musl-bsd-headers"]
pkgdesc = "Main loop library"
license = "ISC"
url = "https://github.com/any1/aml"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b2b8f743213af39f40e8bc611147d69e2ea9e010b9b19cb65246582338f28d96"


def post_install(self):
    self.install_license("COPYING")


@subpackage("aml-devel")
def _(self):
    return self.default_devel()
