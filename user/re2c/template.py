pkgname = "re2c"
pkgver = "4.1"
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
sha256 = "439c5ca02f2dcc280d01054622272f34d54c05919a41859614ec386cc7f89b6d"


def post_install(self):
    self.install_license("LICENSE")
