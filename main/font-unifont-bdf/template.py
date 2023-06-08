pkgname = "font-unifont-bdf"
pkgver = "15.0.06"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs - BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "93cb54fa103a00e25cd3e16550b4b4eb13cbd098e515679ade3ae82cd0739f29"


def do_install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
