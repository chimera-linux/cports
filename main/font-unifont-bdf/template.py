pkgname = "font-unifont-bdf"
pkgver = "16.0.01"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs"
subdesc = "BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "230a0959aa50778b68239c88ad3c2d53abde58be0932b14a379a3869118aca33"


def install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
