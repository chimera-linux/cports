pkgname = "android-udev-rules"
pkgver = "20241109"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "178251de2683dfe27d8bfd2259bc0bc8e38e68b3bc780baca68b8ae9d3d18aca"
options = ["!splitudev"]


def install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
