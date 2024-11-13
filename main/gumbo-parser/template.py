pkgname = "gumbo-parser"
pkgver = "0.12.2"
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
sha256 = "7515dfef24c288fe1230c7b3beef15f09289ed1ac8a926ff249495260e4a1336"


@subpackage("gumbo-parser-devel")
def _(self):
    return self.default_devel()
