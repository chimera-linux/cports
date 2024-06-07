pkgname = "lua5.4-luasystem"
pkgver = "0.3.0"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = ["gmake"]
makedepends = ["lua5.4-devel"]
pkgdesc = "Platform independent system calls for Lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "http://lunarmodules.github.io/luasystem"
source = f"https://github.com/lunarmodules/luasystem/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d3686cbb8c370e71864a13dce8240bc54a1b3ca4ab9d108190c8d115dce7fba0"
# no tests
options = ["!check"]


def init_configure(self):
    cfl = self.get_cflags(shell=True)
    ldfl = self.get_ldflags(shell=True)
    fl = [
        "prefix=/usr",
        "LUA_VERSION=5.4",
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
        f"MYCFLAGS={cfl}",
        f"MYLDFLAGS={cfl} {ldfl}",
        f"LUAINC_linux={self.profile().sysroot}/usr/include/lua5.4",
    ]
    self.make_build_args += fl
    self.make_install_args += fl


def post_install(self):
    self.install_file("system/init.lua", "usr/share/lua/5.4", name="system.lua")
    self.install_license("LICENSE.md")
