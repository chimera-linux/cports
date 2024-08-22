pkgname = "utf8proc"
pkgver = "2.9.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Clean C library for processing UTF-8 Unicode data"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://github.com/JuliaStrings/utf8proc"
source = f"{url}/archive/v{pkgver}/utf8proc-{pkgver}.tar.gz"
sha256 = "18c1626e9fc5a2e192311e36b3010bfc698078f692888940f1fa150547abb0c1"
hardening = ["vis", "cfi"]
# cannot run check because Julia isn't packaged
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("utf8proc-devel")
def _(self):
    return self.default_devel()
