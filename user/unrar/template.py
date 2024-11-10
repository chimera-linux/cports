pkgname = "unrar"
pkgver = "7.1.1"
pkgrel = 0
build_style = "makefile"
make_use_env = True
pkgdesc = "Unarchiver for .rar files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:unrar"
url = "https://www.rarlab.com/rar_add.htm"
source = f"https://www.rarlab.com/rar/unrarsrc-{pkgver}.tar.gz"
sha256 = "2e9cbc9d1c250b40f4a7a6a363b6ccfa3703e190534979d18c8c4ac5ae35dafc"
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
