pkgname = "android-udev-rules"
pkgver = "20250525"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "582bf8daa23f318047e77ece4c101c8696fd9151c459f695dca56cf4a40a72a2"
options = ["!splitudev"]


def install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
