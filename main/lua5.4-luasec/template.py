pkgname = "lua5.4-luasec"
pkgver = "1.3.2"
pkgrel = 0
build_style = "makefile"
make_build_target = "linux"
make_build_args = [
    "LUAPATH=/usr/share/lua/5.4",
    "LUACPATH=/usr/lib/lua/5.4",
]
make_install_args = [*make_build_args]
make_use_env = True
makedepends = ["lua5.4-devel", "openssl3-devel"]
pkgdesc = "Bindings to openssl for lua"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/lunarmodules/luasec"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "97293092ba385ab390decb6678bc8cbeffd5899bfbc49eb7ef4aa00f5e31c3d4"
# no tests defined
options = ["!check"]


def init_configure(self):
    self.tool_flags["CFLAGS"] += [
        f"-I{self.profile().sysroot / 'usr/include/lua5.4'}"
    ]


def post_install(self):
    self.install_license("LICENSE")
