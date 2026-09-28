pkgname = "twolame"
pkgver = "0.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libsndfile-devel"]
checkdepends = ["perl"]
pkgdesc = "Optimized MPEG Audio Layer 2 encoder"
license = "LGPL-2.1-or-later"
url = "https://www.twolame.org"
source = f"$(SOURCEFORGE_SITE)/twolame/twolame-{pkgver}.tar.gz"
sha256 = "cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d"


@subpackage("twolame-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
