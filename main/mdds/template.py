pkgname = "mdds"
pkgver = "3.2.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "slibtool"]
checkdepends = ["boost-devel"]
pkgdesc = "Collection of multi-dimensional data structures"
license = "MIT"
url = "https://gitlab.com/mdds/mdds"
source = f"https://gitlab.com/api/v4/projects/mdds%2Fmdds/packages/generic/source/{pkgver}/mdds-{pkgver}.tar.gz"
sha256 = "3dcb6805c561a0bba3d463de516577a51afce5a69fcf378941fe193a228ecd1b"


def post_install(self):
    self.install_license("LICENSE")
