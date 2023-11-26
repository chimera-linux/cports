pkgname = "android-udev-rules"
pkgver = "20231124"
pkgrel = 0
pkgdesc = (
    "Android udev rules list aimed to be the most comprehensive on the net"
)
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0de9e2fa5ee2c65d3854c3c796701de1cbf9d47f70fa261bdadba4578632733c"
options = ["!splitudev"]
system_groups = ["adbusers"]


def do_install(self):
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
