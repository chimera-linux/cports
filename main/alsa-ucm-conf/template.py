pkgname = "alsa-ucm-conf"
pkgver = "1.2.16.1"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cbfa3c34add2b22375536362a42a36b1488c1ee82503117730d62524ff653aa0"


def install(self):
    self.install_license("LICENSE")
    self.install_files("ucm2", "usr/share/alsa")
