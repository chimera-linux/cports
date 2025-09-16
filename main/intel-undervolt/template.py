pkgname = "intel-undervolt"
pkgver = "1.7"
pkgrel = 1
archs = ["x86_64"]
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = ["dinit-chimera", "elogind-devel"]
pkgdesc = "Intel CPU undervolting tool"
license = "GPL-3.0-or-later"
url = "https://github.com/kitsunyan/intel-undervolt"
source = f"{url}/archive/{pkgver}/intel-undervolt-{pkgver}.tar.gz"
sha256 = "29a7ebaee4830d65d0b5cefa6d497887d4f23f34659876dfe944f3a020cf33ff"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def configure(self):
    self.do("./configure", "--enable-elogind")


def post_install(self):
    self.install_service(self.files_path / "intel-undervolt")
    self.install_service(self.files_path / "intel-undervolt-loop")
