pkgname = "lua5.4-zlib"
pkgver = "1.3"
pkgrel = 0
build_style = "makefile"
make_build_target = "linux"
make_build_args = ["LUA_VER=5.4"]
hostmakedepends = ["pkgconf"]
makedepends = ["lua5.4-devel", "zlib-ng-compat-devel"]
pkgdesc = "Zlib streaming interface for Lua 5.4"
license = "MIT"
url = "https://github.com/brimworks/lua-zlib"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d026eda33b7c3456696bcecdc0b26d7bd779de4f5a4d4215ebe3897095c6c9c8"
# no test suite
options = ["!check"]


def install(self):
    self.install_license("README")
    self.install_file("zlib.so", "usr/lib/lua/5.4", mode=0o755)
