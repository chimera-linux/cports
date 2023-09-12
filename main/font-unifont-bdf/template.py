pkgname = "font-unifont-bdf"
pkgver = "15.1.01"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs - BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "9019b5ecced52a2ca46e81316c1cbaca1b47d8871d9ff5e413c0686e0e47a11d"


def do_install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
