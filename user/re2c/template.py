pkgname = "re2c"
pkgver = "4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "bison",
    "gm4",
    "python",
    "python-docutils",
    "slibtool",
]
pkgdesc = "Regular Expressions to Code, lexer generator"
license = "custom:none"  # Public Domain dedication
url = "https://re2c.org"
source = f"https://github.com/skvadrik/re2c/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "39cd7048a817cf3d7d0c2e58a52fb3597d6e1bc86b1df32b8a3cd755c458adfd"


def post_install(self):
    self.install_license("LICENSE")
