pkgname = "android-udev-rules"
pkgver = "20240829"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "01a9beab08b2436df90d76ba54e092925554a9a842281fd57275b622a6feed0c"
options = ["!splitudev"]


def install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
