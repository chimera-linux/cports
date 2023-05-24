pkgname = "alsa-ucm-conf"
pkgver = "1.2.9"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1c40618161bc2738c55aab4dee1d0c82514e257116f296815a799adeaab5e48b"


def do_install(self):
    self.install_files("ucm2", "usr/share/alsa")
