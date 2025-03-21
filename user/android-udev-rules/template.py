pkgname = "android-udev-rules"
pkgver = "20250314"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a1b3b6055cdb74a013fe3afcfe1e505bc6ca6339f05d64410660d37f1aca2c8d"
options = ["!splitudev"]


def install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
