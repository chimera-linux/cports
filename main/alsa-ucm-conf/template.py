pkgname = "alsa-ucm-conf"
pkgver = "1.2.16"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "43ad2f390c760f6a0f2c0b7547175c780d6572ea77a08dd90855861279a74db6"


def install(self):
    self.install_license("LICENSE")
    self.install_files("ucm2", "usr/share/alsa")
