pkgname = "fennel"
pkgver = "1.4.2"
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
sha256 = "d507e6a99d856c73ddef117ec8dddcb614d42a424b0dbb8f84a4487b63ecac4c"


def post_install(self):
    self.install_license("LICENSE")
