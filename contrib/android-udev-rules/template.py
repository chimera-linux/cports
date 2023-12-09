pkgname = "android-udev-rules"
pkgver = "20231207"
pkgrel = 0
pkgdesc = (
    "Android udev rules list aimed to be the most comprehensive on the net"
)
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/M0Rf30/android-udev-rules"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f8f5513e08cd0e9299ba707c9acc5dec53b9cbdc255d4bfd83abfd378928b6e6"
options = ["!splitudev"]
system_groups = ["adbusers"]


def do_install(self):
    self.install_file("51-android.rules", "usr/lib/udev/rules.d")
