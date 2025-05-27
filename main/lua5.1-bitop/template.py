pkgname = "lua5.1-bitop"
pkgver = "1.0.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
makedepends = ["lua5.1-devel"]
pkgdesc = "Lua module for bitwise operations"
license = "MIT"
url = "https://bitop.luajit.org"
source = f"{url}/download/LuaBitOp-{pkgver}.tar.gz"
sha256 = "d514a3d2cefa76c8d11c1b9ec740d5fae316a9c9764e1e12ddea21e4982fab4b"


def install(self):
    self.install_license("README")
    self.install_file("bit.so", "usr/lib/lua/5.1", mode=0o755)
