pkgname = "fennel"
pkgver = "1.6.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = ["lua5.4"]
depends = ["lua5.4"]
pkgdesc = "Programming language built on top of Lua"
license = "MIT"
url = "https://fennel-lang.org"
source = f"https://git.sr.ht/~technomancy/fennel/archive/{pkgver}.tar.gz"
sha256 = "42942d90bbd68656b6025144bb0527c1ae5a5d55e22a53c7e820325230185bf5"


def post_install(self):
    self.install_license("LICENSE")
