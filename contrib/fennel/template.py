pkgname = "fennel"
pkgver = "1.4.1"
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
sha256 = "89a1a15442f29891f7cc6bdf07d1dc22be983bfe78ccf8c62d6ae2c220fe1af0"


def post_install(self):
    self.install_license("LICENSE")
