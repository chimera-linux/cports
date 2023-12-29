pkgname = "mdds"
pkgver = "2.1.1"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool"]
checkdepends = ["boost-devel"]
pkgdesc = "Collection of multi-dimensional data structures"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.com/mdds/mdds"
source = f"http://kohei.us/files/{pkgname}/src/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8a3767f0a60c53261b5ebbaa717381446813aef8cf28fe9d0ea1371123bbe3f1"


def post_install(self):
    self.install_license("LICENSE")
