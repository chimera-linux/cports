pkgname = "lua5.1-luafilesystem"
pkgver = "1.8.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["LUA_VERSION=5.1"]
make_install_args = ["LUA_VERSION=5.1"]
makedepends = ["lua5.1-devel"]
pkgdesc = "File system library for lua"
license = "MIT"
url = "https://lunarmodules.github.io/luafilesystem"
source = f"https://github.com/lunarmodules/luafilesystem/archive/refs/tags/v{pkgver.replace('.', '_')}.tar.gz"
sha256 = "16d17c788b8093f2047325343f5e9b74cccb1ea96001e45914a58bbae8932495"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
