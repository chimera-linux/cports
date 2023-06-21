pkgname = "xonotic-data"
pkgver = "0.8.5"
pkgrel = 0
pkgdesc = "Free, fast-paced cross-platform first-person shooter (data files)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://xonotic.org"
source = f"https://dl.xonotic.org/xonotic-{pkgver}.zip"
sha256 = "0f92aa238362aeb059b9d9026a9bd38d6217423a35c19f126fb39e38736e37e5"
# no tests
options = ["!check", "!cross"]


def do_install(self):
    self.install_dir("usr/share/xonotic")
    self.install_files("data", "usr/share/xonotic")
    self.install_file("key_0.d0pk", "usr/share/xonotic")
