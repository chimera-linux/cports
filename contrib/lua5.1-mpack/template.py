pkgname = "lua5.1-mpack"
pkgver = "1.0.11"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["USE_SYSTEM_MPACK=1"]
make_check_target = "test"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["lua5.1-devel", "libmpack-devel"]
pkgdesc = "Simple implementation of MessagePack for Lua"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://github.com/libmpack/libmpack-lua"
source = f"https://github.com/libmpack/libmpack-lua/archive/{pkgver}.tar.gz"
sha256 = "1d7181514aef66e6c4cad025ae7bd3f8e354125847e33db2394d91fc8dd3e478"
# checks require to download additional tools (use luarocks)
options = ["!cross", "!check"]


def init_configure(self):
    self.tool_flags["CFLAGS"] += [
        "-DMPACK_USE_SYSTEM",
        f"-I{self.profile().sysroot / 'usr/include/lua5.1'}",
    ]


def do_install(self):
    self.install_license("LICENSE-MIT")
    self.install_dir("usr/lib/lua/5.1")
    self.install_file("mpack.so", "usr/lib/lua/5.1", mode=0o755)
