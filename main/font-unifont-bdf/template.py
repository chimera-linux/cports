pkgname = "font-unifont-bdf"
pkgver = "16.0.02"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs"
subdesc = "BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "521f2b92e8b6bd4ea190cea049a039dde359a6e2cae9458e45d696008fa6997f"


def install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
