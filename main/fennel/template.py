pkgname = "fennel"
pkgver = "1.5.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = ["lua5.4"]
depends = ["lua5.4"]
pkgdesc = "Programming language built on top of Lua"
license = "MIT"
url = "https://fennel-lang.org"
source = f"https://git.sr.ht/~technomancy/fennel/archive/{pkgver}.tar.gz"
sha256 = "0ad230b4919f234e114ae763d179ff9bda8fa55c8833b97b99a1b596f98536ff"


def post_install(self):
    self.install_license("LICENSE")
