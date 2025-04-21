pkgname = "alsa-ucm-conf"
pkgver = "1.2.14"
pkgrel = 0
pkgdesc = "ALSA Use Case Manager topology files"
license = "BSD-3-Clause"
url = "https://github.com/alsa-project/alsa-ucm-conf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a441fcc0bf70d91c52bd208de9b1e30bab9ad336ea5ee361a2b8982133fdb7f7"


def install(self):
    self.install_license("LICENSE")
    self.install_files("ucm2", "usr/share/alsa")
