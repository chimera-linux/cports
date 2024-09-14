pkgname = "lua5.1-bitop"
pkgver = "1.0.2"
pkgrel = 1
build_style = "makefile"
make_check_target = "test"
makedepends = ["lua5.1-devel"]
pkgdesc = "Lua module for bitwise operations"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "http://bitop.luajit.org"
source = f"{url}/download/LuaBitOp-{pkgver}.tar.gz"
sha256 = "1207c9293dcd52eb9dca6538d1b87352bd510f4e760938f5048433f7f272ce99"


def install(self):
    self.install_license("README")
    self.install_file("bit.so", "usr/lib/lua/5.1", mode=0o755)
