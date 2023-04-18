pkgname = "android-udev-rules"
pkgver = "20230614"
pkgrel = 0
pkgdesc = (
    "Android udev rules list aimed to be the most comprehensive on the net"
)
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "563b8f3194110b7173dfaad61e74da2842b28c4f2409dedce04d5572ef2f056f"
options = ["!splitudev"]
system_groups = ["adbusers"]


def do_install(self):
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
