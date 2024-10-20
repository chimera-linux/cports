pkgname = "android-udev-rules"
pkgver = "20241019"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1fdb0aa5db086c371310f97c59191706968c8bf93d8c4a63b0c7a04734fd84df"
options = ["!splitudev"]


def install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
