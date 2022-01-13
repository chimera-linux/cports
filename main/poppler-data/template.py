pkgname = "poppler-data"
pkgver = "0.4.11"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Encoding data for the poppler PDF rendering library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://poppler.freedesktop.org"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "2cec05cd1bb03af98a8b06a1e22f6e6e1a65b1e2f3816cb3069bb0874825f08c"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.adobe")
