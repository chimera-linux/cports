pkgname = "inxi"
pkgver = "3.3.40.1"
pkgrel = 0
depends = ["perl"]
pkgdesc = "Fully featured CLI system information tool"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/smxi/inxi"
source = f"{url}/archive/{pkgver[: pkgver.rfind('.')]}-{pkgver[pkgver.rfind('.') + 1 :]}.tar.gz"
sha256 = "b3f307f06c3b969bd65151d39729b97a767af42fddd3d9bab971135c0e7cd873"


def install(self):
    self.install_bin("inxi")
    self.install_man("inxi.1")
