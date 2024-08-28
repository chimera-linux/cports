pkgname = "font-unifont-bdf"
pkgver = "15.1.05"
pkgrel = 1
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs"
subdesc = "BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "8ea5b5a14d71e3353d1fea373f5d88d198ad1e285cedd8294655926ee11fd91d"


def install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
