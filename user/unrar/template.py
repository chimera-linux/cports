pkgname = "unrar"
pkgver = "7.1.6"
pkgrel = 0
build_style = "makefile"
make_use_env = True
pkgdesc = "Unarchiver for .rar files"
license = "custom:unrar"
url = "https://www.rarlab.com/rar_add.htm"
source = f"https://www.rarlab.com/rar/unrarsrc-{pkgver}.tar.gz"
sha256 = "ca5e1da37dd6fa1b78bb5ed675486413f79e4a917709744aa04b6f93dfd914f0"
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
