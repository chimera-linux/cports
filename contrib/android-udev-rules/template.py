pkgname = "android-udev-rules"
pkgver = "20231104"
pkgrel = 0
pkgdesc = (
    "Android udev rules list aimed to be the most comprehensive on the net"
)
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2f2e82c8d352d45a93806bc776df518da59c19ee9f0bf6aa8606d5d3ae05eccf"
options = ["!splitudev"]
system_groups = ["adbusers"]


def do_install(self):
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
