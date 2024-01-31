pkgname = "alsa-ucm-conf"
pkgver = "1.2.11"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "67f96e2177fe0ce9e90e75734cffc805a375b988e77c7615879dfb35dd4031d5"


def do_install(self):
    self.install_license("LICENSE")
    self.install_files("ucm2", "usr/share/alsa")
