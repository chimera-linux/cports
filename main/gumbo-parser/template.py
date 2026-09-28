pkgname = "gumbo-parser"
pkgver = "0.13.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["gtest-devel"]
pkgdesc = "HTML5 parsing library in pure C99"
license = "Apache-2.0"
url = "https://codeberg.org/gumbo-parser/gumbo-parser"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "dbdc159dc8e5c6f3f254e50bce689dd9e439064ff06c165d5653410a5714ab66"


@subpackage("gumbo-parser-devel")
def _(self):
    return self.default_devel()
