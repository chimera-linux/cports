pkgname = "libuninameslist"
pkgver = "20240910"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library of Unicode names and annotation data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/fontforge/libuninameslist"
source = (
    f"{url}/releases/download/{pkgver}/libuninameslist-dist-{pkgver}.tar.gz"
)
sha256 = "e59aab324ca0a3a713fe85c09a56c40c680a8458438d90624597920b3ef0be26"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuninameslist-devel")
def _(self):
    return self.default_devel()
