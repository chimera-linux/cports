pkgname = "gumbo-parser"
pkgver = "0.13.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["gtest-devel"]
pkgdesc = "HTML5 parsing library in pure C99"
license = "Apache-2.0"
url = "https://codeberg.org/gumbo-parser/gumbo-parser"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "1a054d1e53d556641a6666537247411a77b0c18ef6ad5df23e30d2131676ef81"


@subpackage("gumbo-parser-devel")
def _(self):
    return self.default_devel()
