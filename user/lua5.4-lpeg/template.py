pkgname = "lua5.4-lpeg"
pkgver = "1.1.0"
pkgrel = 0
build_style = "makefile"
make_build_target = "lpeg.so"
make_check_target = "test"
makedepends = ["lua5.4-devel"]
pkgdesc = "Pattern-matching library based on Parsing Expression Grammars"
license = "MIT"
url = "https://www.inf.puc-rio.br/~roberto/lpeg"
source = f"{url}/lpeg-{pkgver}.tar.gz"
sha256 = "4b155d67d2246c1ffa7ad7bc466c1ea899bbc40fef0257cc9c03cecbaed4352a"
# for check
exec_wrappers = [("/usr/bin/lua5.4", "lua")]


def init_configure(self):
    self.tool_flags["CFLAGS"] += [
        f"-I{self.profile().sysroot / 'usr/include/lua5.4'}",
        "-fPIC",
    ]


def install(self):
    self.install_license("lpeg.html")
    self.install_dir("usr/lib/lua/5.4")
    self.install_file("lpeg.so", "usr/lib/lua/5.4", mode=0o755)
    self.install_dir("usr/share/lua/5.4")
    self.install_file("re.lua", "usr/share/lua/5.4")
