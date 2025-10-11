pkgname = "unrar"
pkgver = "7.1.10"
pkgrel = 0
build_style = "makefile"
make_use_env = True
pkgdesc = "Unarchiver for .rar files"
license = "custom:unrar"
url = "https://www.rarlab.com/rar_add.htm"
source = f"https://www.rarlab.com/rar/unrarsrc-{pkgver}.tar.gz"
sha256 = "72a9ccca146174f41876e8b21ab27e973f039c6d10b13aabcb320e7055b9bb98"
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
