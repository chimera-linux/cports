pkgname = "lua5.1-lpeg"
pkgver = "1.0.2"
pkgrel = 0
build_style = "makefile"
make_build_target = "lpeg.so"
make_check_target = "test"
makedepends = ["lua5.1-devel"]
pkgdesc = "Pattern-matching library based on Parsing Expression Grammars"
license = "MIT"
url = "http://www.inf.puc-rio.br/~roberto/lpeg"
source = f"{url}/lpeg-{pkgver}.tar.gz"
sha256 = "48d66576051b6c78388faad09b70493093264588fcd0f258ddaab1cdd4a15ffe"
# for check
exec_wrappers = [("/usr/bin/lua5.1", "lua")]

def init_configure(self):
    self.tool_flags["CFLAGS"] += [
        f"-I{ self.profile().sysroot / 'usr/include/lua5.1'}",
        "-fPIC"
    ]

def do_install(self):
    self.install_license("lpeg.html")
    self.install_dir("usr/lib/lua/5.1")
    self.install_file("lpeg.so", "usr/lib/lua/5.1", mode = 0o755)
    self.install_dir("usr/share/lua/5.1")
    self.install_file("re.lua", "usr/share/lua/5.1")
