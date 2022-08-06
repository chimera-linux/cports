pkgname = "dinit-chimera"
_commit = "539c3e4fdd56f167fd93528b4e12d7973d4e0c16"
pkgver = "0.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
depends = ["dinit", "util-linux", "eudev"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "1d8325735a29becf5f86466b8cf03d8a74498e2562065f5ae9b7062fc429eecc"
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "os-release", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_link("dinit", "usr/bin/init")
