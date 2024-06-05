pkgname = "lua5.4-lua-term"
pkgver = "0.08"
pkgrel = 0
makedepends = ["lua5.4-devel"]
pkgdesc = "Terminal operations for Lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/hoelzro/lua-term"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8ff94f390ea9d98c734699373ca3b0ce500d651b2ab1cb8d7d2336fc5b79cded"


def do_build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)
    cc.invoke(
        ["core.c"],
        "core.so",
        flags=[f"-I{self.profile().sysroot / 'usr/include/lua5.4'}", "-fPIC"],
        ldflags=["-shared"],
    )


def do_install(self):
    self.install_dir("usr/lib/lua/5.4")
    self.install_file("core.so", "usr/lib/lua/5.4/term")
    self.install_dir("usr/share/lua/5.4")
    self.install_files("term", "usr/share/lua/5.4")
    self.install_license("COPYING")
