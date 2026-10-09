pkgname = "utf8proc"
pkgver = "2.12.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Clean C library for processing UTF-8 Unicode data"
license = "MIT"
url = "https://github.com/JuliaStrings/utf8proc"
source = f"{url}/archive/v{pkgver}/utf8proc-{pkgver}.tar.gz"
sha256 = "f564011d38b2888d583d510b08e69ffa15aa117155db1b9b49ef1dfe1fa25111"
hardening = ["vis", "cfi"]
# cannot run check because Julia isn't packaged
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("utf8proc-devel")
def _(self):
    return self.default_devel()
