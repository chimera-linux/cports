pkgname = "re2c"
pkgver = "4.2"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "bison",
    "gm4",
    "python",
    "slibtool",
    "python-docutils",
]
pkgdesc = "Regular Expressions to Code, lexer generator"
license = "custom:none"  # Public Domain dedication
url = "https://re2c.org"
source = f"https://github.com/skvadrik/re2c/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "01b56c67ca2d5054b1aafc41ef5c15c50fbb6a7e760b1b2346e6116ef039525e"


def post_install(self):
    self.install_license("LICENSE")
