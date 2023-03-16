pkgname = "libpipeline"
pkgver = "1.5.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["check-devel"]
pkgdesc = "Pipeline manipulation library"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://libpipeline.gitlab.io/libpipeline"
source = f"https://download.savannah.nongnu.org/releases/libpipeline/libpipeline-{pkgver}.tar.gz"
sha256 = "b8b45194989022a79ec1317f64a2a75b1551b2a55bea06f67704cb2a2e4690b0"

@subpackage("libpipeline-devel")
def _devel(self):
    return self.default_devel()
