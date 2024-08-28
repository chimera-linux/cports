pkgname = "lua5.4-zlib"
pkgver = "1.2"
pkgrel = 0
build_style = "makefile"
make_build_target = "linux"
make_build_args = ["LUA_VER=5.4"]
hostmakedepends = ["pkgconf"]
makedepends = ["lua5.4-devel", "zlib-ng-compat-devel"]
pkgdesc = "Zlib streaming interface for Lua 5.4"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/brimworks/lua-zlib"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "26b813ad39c94fc930b168c3418e2e746af3b2e80b92f94f306f6f954cc31e7d"
# no test suite
options = ["!check"]


def install(self):
    self.install_license("README")
    self.install_file("zlib.so", "usr/lib/lua/5.4", mode=0o755)
