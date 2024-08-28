pkgname = "alsa-ucm-conf"
pkgver = "1.2.12"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ad8dd8d79bda54f9d28b095ce9dfa009de9970daf7b57dda86216a4e4977fe4e"


def install(self):
    self.install_license("LICENSE")
    self.install_files("ucm2", "usr/share/alsa")
