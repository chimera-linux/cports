pkgname = "vmtouch"
pkgver = "1.3.1"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["perl"]
pkgdesc = "Filesystem cache diagnostic and control tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://hoytech.com/vmtouch"
source = (
    f"https://github.com/hoytech/vmtouch/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "d57b7b3ae1146c4516429ab7d6db6f2122401db814ddd9cdaad10980e9c8428c"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def do_install(self):
    self.install_bin("vmtouch")
    self.install_man("vmtouch.8")
    self.install_license("LICENSE")
