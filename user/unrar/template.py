pkgname = "unrar"
pkgver = "7.2.6"
pkgrel = 0
build_style = "makefile"
make_use_env = True
pkgdesc = "Unarchiver for .rar files"
license = "custom:unrar"
url = "https://www.rarlab.com/rar_add.htm"
source = f"https://www.rarlab.com/rar/unrarsrc-{pkgver}.tar.gz"
sha256 = "d1afa67ef4121ebc5986815699e05db0ce8648499e5dca854f282a4c3f72c003"
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
