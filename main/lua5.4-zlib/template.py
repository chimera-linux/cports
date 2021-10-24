pkgname = "lua5.4-zlib"
pkgver = "1.2"
pkgrel = 0
build_style = "makefile"
make_build_target = "linux"
hostmakedepends = ["pkgconf"]
makedepends = ["lua5.4-devel", "zlib-devel"]
pkgdesc = "Zlib streaming interface for Lua (5.4)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/brimworks/lua-zlib"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "26b813ad39c94fc930b168c3418e2e746af3b2e80b92f94f306f6f954cc31e7d"
# no test suite
options = ["!check"]

def init_configure(self):
    eargs = [
        "LIBS=-lz -llua5.4 -lm",
        "INCDIR=-I/usr/include -I/usr/include/lua5.4",
        "LIBDIR=-L/usr/lib",
        "LUACPATH=/usr/lib/lua/5.4",
        "LUAPATH=/usr/share/lua/5.4",
    ]
    self.make_build_args += eargs
    self.make_install_args += eargs
    self.make_check_args += eargs
    self.tools["LD"] = self.get_tool("CC")
    self.tool_flags["LDFLAGS"] = self.get_cflags(["-shared"])

def do_install(self):
    self.install_license("README")
    self.install_file("zlib.so", "usr/lib/lua/5.4", mode = 0o755)
