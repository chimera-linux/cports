pkgname = "libxmlb"
pkgver = "0.3.12"
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
sha256 = "b1e61f64dadc67e458430bb35a9f1b25170aafcf5674a52012ae38a2212227b3"
options = ["!cross"]


@subpackage("libxmlb-devel")
def _devel(self):
    return self.default_devel()
