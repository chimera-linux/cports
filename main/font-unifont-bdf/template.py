pkgname = "font-unifont-bdf"
pkgver = "16.0.03"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs"
subdesc = "BDF"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "7f3d1664ac1c051f59a1a1360dd654f78d82c246a688c342e863cec7f6ba95d4"


def install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
