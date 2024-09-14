pkgname = "fennel"
pkgver = "1.5.1"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = ["lua5.4"]
depends = ["lua5.4"]
pkgdesc = "Programming language built on top of Lua"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://fennel-lang.org"
source = f"https://git.sr.ht/~technomancy/fennel/archive/{pkgver}.tar.gz"
sha256 = "78c457c5e11dd78b5818f74fd49789acfed374e0a8d7a1f3ef71e166030b2905"


def post_install(self):
    self.install_license("LICENSE")
