pkgname = "gumbo-parser"
pkgver = "0.12.1"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "gm4",
    "libtool",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "HTML5 parsing library in pure C99"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://codeberg.org/gumbo-parser/gumbo-parser"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c0bb5354e46539680724d638dbea07296b797229a7e965b13305c930ddc10d82"


@subpackage("gumbo-parser-devel")
def _(self):
    return self.default_devel()
