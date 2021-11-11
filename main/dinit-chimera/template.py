pkgname = "dinit-chimera"
_commit = "527472d79cb9c694037439f378a1eda0d90d5c1a"
pkgver = "0.1"
pkgrel = 0
build_style = "makefile"
depends = ["dinit", "util-linux"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "f2915118d2eba04fa5a947f6be64af9d9e4cfeb149f85e0357642cf21428f1a5"
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "os-release", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_link("dinit", "usr/bin/init")
