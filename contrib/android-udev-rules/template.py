pkgname = "android-udev-rules"
pkgver = "20240114"
pkgrel = 0
pkgdesc = (
    "Android udev rules list aimed to be the most comprehensive on the net"
)
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ba50560820ff89035068600f935d669068af7e507e560c7f4d9a1bc77fbf4636"
options = ["!splitudev"]


def do_install(self):
    self.install_file(self.files_path / "adbusers.conf", "usr/lib/sysusers.d")
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
