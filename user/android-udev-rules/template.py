pkgname = "android-udev-rules"
pkgver = "20260922"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3cc14f34142e71837eb073cc10b09eb48a9f7282b7c9ade9259e7809eec5062e"
options = ["!splitudev"]


def install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
