pkgname = "twolame"
pkgver = "0.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libsndfile-devel"]
checkdepends = ["perl"]
pkgdesc = "Optimized MPEG Audio Layer 2 encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.twolame.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d"


@subpackage("twolame-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/doc"])


configure_gen = []
