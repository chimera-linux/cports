pkgname = "font-unifont-bdf"
pkgver = "14.0.04"
pkgrel = 0
depends = ["font-util"]
pkgdesc = "GNU Unifont Glyphs - BDF"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://unifoundry.com/unifont/index.html"
source = f"http://unifoundry.com/pub/unifont/unifont-{pkgver}/font-builds/unifont-{pkgver}.bdf.gz"
sha256 = "0bad2b8a46fcc4864c7b4cee4072653a58b9f36e2f54a5a395c7d6dc97766526"

def do_install(self):
    self.install_file(
        f"unifont-{pkgver}.bdf", "usr/share/fonts/misc",
        name = "unifont.bdf"
    )
