pkgname = "android-udev-rules"
pkgver = "20240625"
pkgrel = 0
pkgdesc = "Comprehensive Android udev rules collection"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9ed9f34b07082c9bb609c09a922dfd1e2df7cee7ccee0584bfc95da18c88eafe"
options = ["!splitudev"]


def install(self):
    self.install_sysusers(self.files_path / "adbusers.conf", name="adbusers")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
