pkgname = "font-unifont-bdf"
pkgver = "15.1.02"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs - BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "912834ab9cd372f300541894615f910af4db82477c91b236674057eadfc76429"


def do_install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc", name="unifont.bdf"
    )
