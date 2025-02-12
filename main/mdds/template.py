pkgname = "mdds"
pkgver = "3.0.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "slibtool"]
checkdepends = ["boost-devel"]
pkgdesc = "Collection of multi-dimensional data structures"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.com/mdds/mdds"
source = f"https://gitlab.com/api/v4/projects/mdds%2Fmdds/packages/generic/source/{pkgver}/mdds-{pkgver}.tar.gz"
sha256 = "e8660f5510f099af1cc9bbcd2c1f12493b72b24f82616d70f9d71ab6ce1258ec"


def post_install(self):
    self.install_license("LICENSE")
