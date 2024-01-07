pkgname = "alsa-ucm-conf"
pkgver = "1.2.10"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "00e67c31b60494665f45ce57ca9d2c42421c40fbe0140b5a5648291238e63508"


def do_install(self):
    self.install_license("LICENSE")
    self.install_files("ucm2", "usr/share/alsa")
