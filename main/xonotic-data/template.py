pkgname = "xonotic-data"
pkgver = "0.8.6"
pkgrel = 0
pkgdesc = "Free, fast-paced cross-platform first-person shooter"
subdesc = "data files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://xonotic.org"
source = f"https://dl.xonotic.org/xonotic-{pkgver}.zip"
sha256 = "50850f8d800e7499722f6ea61e478e96464a375494b5a24da93aa0598cbe964d"
# no tests
options = ["!check", "!cross"]


def install(self):
    self.install_dir("usr/share/xonotic")
    self.install_files("data", "usr/share/xonotic")
    self.install_file("key_0.d0pk", "usr/share/xonotic")
