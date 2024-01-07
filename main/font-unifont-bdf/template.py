pkgname = "font-unifont-bdf"
pkgver = "15.1.04"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs - BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "88e00954b10528407e62e97ce6eaa88c847ebfd9a464cafde6bf55c7e4eeed54"


def do_install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
