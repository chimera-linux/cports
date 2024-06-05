pkgname = "lua5.4-luasystem"
pkgver = "0.3.0"
pkgrel = 0
makedepends = ["lua5.4-devel"]
pkgdesc = "Platform independent system calls for Lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "http://lunarmodules.github.io/luasystem"
source = f"https://github.com/lunarmodules/luasystem/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d3686cbb8c370e71864a13dce8240bc54a1b3ca4ab9d108190c8d115dce7fba0"


def do_build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)
    cc.invoke(
        [
            "src/core.c",
            "src/compat.c",
            "src/time.c",
            "src/environment.c",
            "src/random.c",
            "src/term.c",
        ],
        "system.so",
        flags=[f"-I{self.profile().sysroot / 'usr/include/lua5.4'}", "-fPIC"],
        ldflags=["-shared"],
    )


def do_install(self):
    self.install_dir("usr/lib/lua/5.4")
    self.install_file("system.so", "usr/lib/lua/5.4")
    self.install_dir("usr/share/lua/5.4")
    self.install_file("system/init.lua", "usr/share/lua/5.4", name="system.lua")
    self.install_license("LICENSE.md")
