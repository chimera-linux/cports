pkgname = "lua5.1-luasocket"
pkgver = "3.1.0"
pkgrel = 0
build_style = "makefile"
make_dir = "src"
make_build_target = "linux"
make_build_args = ["LUAV=5.1", "PLAT=linux"]
make_install_target = "install-unix"
make_install_args = [*make_build_args]
make_use_env = True
makedepends = ["lua5.1-devel"]
pkgdesc = "Networking library for lua"
license = "MIT"
url = "https://lunarmodules.github.io/luasocket"
source = f"https://github.com/lunarmodules/luasocket/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bf033aeb9e62bcaa8d007df68c119c966418e8c9ef7e4f2d7e96bddeca9cca6e"
env = {"LUAPREFIX_linux": "/usr"}
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
