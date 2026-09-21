pkgname = "utf8proc"
pkgver = "2.11.3"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Clean C library for processing UTF-8 Unicode data"
license = "MIT"
url = "https://github.com/JuliaStrings/utf8proc"
source = f"{url}/archive/v{pkgver}/utf8proc-{pkgver}.tar.gz"
sha256 = "abfed50b6d4da51345713661370290f4f4747263ee73dc90356299dfc7990c78"
hardening = ["vis", "cfi"]
# cannot run check because Julia isn't packaged
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("utf8proc-devel")
def _(self):
    return self.default_devel()
