pkgname = "lua5.4-luassert"
pkgver = "1.9.0"
pkgrel = 0
depends = ["lua5.4-say"]
pkgdesc = "Assertion library for Lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/lunarmodules/luassert"
source = f"https://github.com/lunarmodules/luassert/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1db0fabf1bd87392860375b89a8a37d17b687325c988be0df8c42e7e96e7ed73"


def install(self):
    self.install_files("src", "usr/share/lua/5.4", name="luassert")
    self.install_license("LICENSE")
