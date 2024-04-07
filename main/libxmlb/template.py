pkgname = "libxmlb"
pkgver = "0.3.17"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtkdoc=false"]
hostmakedepends = ["pkgconf", "meson", "gobject-introspection"]
makedepends = ["xz-devel", "zstd-devel"]
checkdepends = ["shared-mime-info"]
depends = ["shared-mime-info"]
pkgdesc = "Library to help create and query binary XML blobs"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libxmlb"
source = f"https://github.com/hughsie/libxmlb/releases/download/{pkgver}/libxmlb-{pkgver}.tar.xz"
sha256 = "bdaf38779646e436cba73caf2bdc1ea07226e6ce418a01800595cd4702cc3caa"
options = ["!cross"]


@subpackage("libxmlb-devel")
def _devel(self):
    return self.default_devel()
