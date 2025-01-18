pkgname = "unrar"
pkgver = "7.1.3"
pkgrel = 0
build_style = "makefile"
make_use_env = True
pkgdesc = "Unarchiver for .rar files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:unrar"
url = "https://www.rarlab.com/rar_add.htm"
source = f"https://www.rarlab.com/rar/unrarsrc-{pkgver}.tar.gz"
sha256 = "f7edb6f55fb53611206781d9e56f2625ef4411a6b129768800196617d9df920a"
# no tests
options = ["!check"]


def init_build(self):
    eargs = [
        "CXX=" + self.get_tool("CXX"),
        "LD=" + self.get_tool("LD"),
        "STRIP=/usr/bin/true",
        "-f",
        "makefile",
    ]
    self.make_build_args += eargs
    self.make_install_args += eargs


def install(self):
    self.install_bin("unrar")
    self.install_license("license.txt")
