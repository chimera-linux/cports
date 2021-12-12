pkgname = "dinit-chimera"
_commit = "f79c07c10b4462174a5631ba37b7a569c19f4756"
pkgver = "0.1"
pkgrel = 0
build_style = "makefile"
depends = ["dinit", "util-linux", "eudev"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "e10ac422ccac11a2c9542e4a5bbc74f5b4c7d045fbd751bb4d23d767d613e75d"
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "os-release", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_link("dinit", "usr/bin/init")
