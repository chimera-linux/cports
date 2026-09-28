pkgname = "font-unifont-bdf"
pkgver = "16.0.04"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs"
subdesc = "BDF"
license = "GPL-2.0-or-later"
url = "https://unifoundry.com/unifont/index.html"
source = f"https://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "4a1689c0065666ac70e1310420ce67d7fa3dcf83c1a2e1e6b2c115aa22deb3cf"


def install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
