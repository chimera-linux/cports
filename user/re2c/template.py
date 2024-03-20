pkgname = "re2c"
pkgver = "4.0.2"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "bison",
    "gm4",
    "python",
    "slibtool",
    "python-docutils",
]
pkgdesc = "Regular Expressions to Code, lexer generator"
maintainer = "ttyyls <contact@behri.org>"
license = "custom:none"  # Public Domain dedication
url = "https://re2c.org"
source = f"https://github.com/skvadrik/re2c/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "43f15eef0dd2b67b268b520a40bb440bb78a0ad77b11e7fd2ee16b2c35ce6485"


def post_install(self):
    self.install_license("LICENSE")
