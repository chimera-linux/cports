pkgname = "alsa-ucm-conf"
pkgver = "1.2.13"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0b1c6740c665078a1c2818ef4902417d75bba4f0fb7fd558633707c367a727e7"


def install(self):
    self.install_license("LICENSE")
    self.install_files("ucm2", "usr/share/alsa")
