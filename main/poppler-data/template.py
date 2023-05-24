pkgname = "poppler-data"
pkgver = "0.4.12"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Encoding data for the poppler PDF rendering library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://poppler.freedesktop.org"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c835b640a40ce357e1b83666aabd95edffa24ddddd49b8daff63adb851cdab74"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.adobe")
