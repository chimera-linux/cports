pkgname = "lua5.4-lua-term"
pkgver = "0.08"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["LUA_VER=5.4"]
make_install_args = ["LUA_VER=5.4"]
make_use_env = True
hostmakedepends = ["gmake"]
makedepends = ["lua5.4-devel"]
pkgdesc = "Terminal operations for Lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/hoelzro/lua-term"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8ff94f390ea9d98c734699373ca3b0ce500d651b2ab1cb8d7d2336fc5b79cded"
# no tests
options = ["!check"]


def init_configure(self):
    self.make_install_args += [f"LUA_DIR={self.chroot_destdir / 'usr'}"]


def post_install(self):
    self.install_license("COPYING")
