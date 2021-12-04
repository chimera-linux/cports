pkgname = "font-unifont-bdf"
pkgver = "14.0.01"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs (BDF)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "391d194f6307fcd0915daafd360509a734e26f3e4013e63d47deb2530d59e66e"

def do_install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc",
        name = "unifont.bdf"
    )
