pkgname = "gumbo-parser"
pkgver = "0.13.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "gm4",
    "slibtool",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "HTML5 parsing library in pure C99"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://codeberg.org/gumbo-parser/gumbo-parser"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "7ad2ee259f35e8951233e4c9ad80968fb880f20d8202cb9c48f0b65f67d38e61"


@subpackage("gumbo-parser-devel")
def _(self):
    return self.default_devel()
