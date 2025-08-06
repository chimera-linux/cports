pkgname = "mdds"
pkgver = "3.1.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "slibtool"]
checkdepends = ["boost-devel"]
pkgdesc = "Collection of multi-dimensional data structures"
license = "MIT"
url = "https://gitlab.com/mdds/mdds"
source = f"https://gitlab.com/api/v4/projects/mdds%2Fmdds/packages/generic/source/{pkgver}/mdds-{pkgver}.tar.gz"
sha256 = "53fdc421b11fb7dda26591eace89b52eb0bdbbb8c8e6f05b6a66dfb55a29a4b6"


def post_install(self):
    self.install_license("LICENSE")
