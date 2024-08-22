pkgname = "fennel"
pkgver = "1.5.0"
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
sha256 = "96c8cb1ed78597dd3c58b969dda7273fda30bb707b337394fe806d285883b3c3"


def post_install(self):
    self.install_license("LICENSE")
