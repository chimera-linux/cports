pkgname = "fennel"
pkgver = "1.4.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "lua5.4"]
depends = ["lua5.4"]
pkgdesc = "Programming language built on top of Lua"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://fennel-lang.org"
source = f"https://git.sr.ht/~technomancy/fennel/archive/{pkgver}.tar.gz"
sha256 = "375892126dae7fa80f727db613ccb7480d18c958cd00f9f6c8c3f82ab1751f98"


def post_install(self):
    self.install_license("LICENSE")
