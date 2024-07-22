pkgname = "intel-undervolt"
pkgver = "1.7"
pkgrel = 0
archs = ["x86_64"]
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["elogind-devel"]
pkgdesc = "Intel CPU undervolting tool"
maintainer = "Sid Pranjale <mail@sidonthe.net>"
license = "GPL-3.0-or-later"
url = "https://github.com/kitsunyan/intel-undervolt"
source = f"{url}/archive/{pkgver}/intel-undervolt-{pkgver}.tar.gz"
sha256 = "29a7ebaee4830d65d0b5cefa6d497887d4f23f34659876dfe944f3a020cf33ff"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def do_configure(self):
    self.do("./configure", "--enable-elogind")


def post_install(self):
    self.install_service(self.files_path / "intel-undervolt")
    self.install_service(self.files_path / "intel-undervolt-loop")
