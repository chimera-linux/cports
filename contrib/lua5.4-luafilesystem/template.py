pkgname = "lua5.4-luafilesystem"
pkgver = "1.8.0"
pkgrel = 0
makedepends = ["lua5.4-devel"]
pkgdesc = "File system library for lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://lunarmodules.github.io/luafilesystem"
source = f"https://github.com/lunarmodules/luafilesystem/archive/refs/tags/v{pkgver.replace('.','_')}.tar.gz"
sha256 = "16d17c788b8093f2047325343f5e9b74cccb1ea96001e45914a58bbae8932495"


def do_build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)
    cc.invoke(
        ["src/lfs.c"],
        "lfs.so",
        flags=[f"-I{self.profile().sysroot / 'usr/include/lua5.4'}", "-fPIC"],
        ldflags=["-shared"],
    )


def do_install(self):
    self.install_dir("usr/lib/lua/5.4")
    self.install_file("lfs.so", "usr/lib/lua/5.4")
    self.install_license("LICENSE")
