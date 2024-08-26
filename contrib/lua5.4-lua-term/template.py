pkgname = "lua5.4-lua-term"
pkgver = "0.8"
pkgrel = 0
build_style = "makefile"
make_build_args = ["LUA_VER=5.4"]
make_install_args = ["LUA_VER=5.4"]
make_use_env = True
makedepends = ["lua5.4-devel"]
pkgdesc = "Terminal operations for Lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/hoelzro/lua-term"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0cb270be22dfc262beec2f4ffc66b878ccaf236f537d693fa36c8f578fc51aa6"
# no tests
options = ["!check"]


def init_configure(self):
    self.make_install_args += [f"LUA_DIR={self.chroot_destdir / 'usr'}"]


def post_install(self):
    self.install_license("COPYING")
