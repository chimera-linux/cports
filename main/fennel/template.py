pkgname = "fennel"
pkgver = "1.6.1"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = ["lua5.4"]
depends = ["lua5.4"]
pkgdesc = "Programming language built on top of Lua"
license = "MIT"
url = "https://fennel-lang.org"
source = f"https://git.sr.ht/~technomancy/fennel/archive/{pkgver}.tar.gz"
sha256 = "f0f188e9a4424851d9263ab69302b6b2ffc5c6efb67a25fffc52187a29c94024"


def post_install(self):
    self.install_license("LICENSE")
