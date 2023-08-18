pkgname = "libxmlb"
pkgver = "0.3.13"
pkgrel = 0
build_style = "meson"
# tests require some file to exist in /tmp? so it fails
configure_args = ["-Dtests=false", "-Dgtkdoc=false"]
hostmakedepends = ["pkgconf", "meson", "cmake", "gobject-introspection"]
makedepends = ["liblzma-devel", "libzstd-devel"]
pkgdesc = "Library to help create and query binary XML blobs"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libxmlb"
source = f"https://github.com/hughsie/libxmlb/releases/download/{pkgver}/libxmlb-{pkgver}.tar.xz"
sha256 = "ae45ae4c0606f94d98fea16b7097b3470e48c2f277954ae9bc4d9d029ed72496"
options = ["!cross"]


@subpackage("libxmlb-devel")
def _devel(self):
    return self.default_devel()
