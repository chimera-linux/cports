pkgname = "lua5.4-penlight"
pkgver = "1.14.0"
pkgrel = 0
makedepends = ["lua5.4-devel"]
depends = ["lua5.4-luafilesystem"]
pkgdesc = "Lua library for miscellaneous extended operations"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://lunarmodules.github.io/Penlight"
source = f"https://github.com/lunarmodules/Penlight/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2387431c0e83c4189cccb35b989141a3280d735cb5d42bacf3451af9869bebf7"


def install(self):
    self.install_dir("usr/share/lua/5.4")
    self.install_files("lua/pl", "usr/share/lua/5.4")
    self.install_license("LICENSE.md")
