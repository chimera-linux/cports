pkgname = "dinit-chimera"
_commit = "bf7e44c0afb8171dc1b1a3b0ca70dce77b954186"
pkgver = "0.1"
pkgrel = 0
build_style = "makefile"
depends = ["dinit", "util-linux"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "3bdd7f768f48a2ac572117b6f5455951854dc4b4c66c6056dd23d11597044ba6"
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "os-release", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_link("dinit", "usr/bin/init")
