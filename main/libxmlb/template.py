pkgname = "libxmlb"
pkgver = "0.3.15"
pkgrel = 0
build_style = "meson"
# tests require some file to exist in /tmp? so it fails
configure_args = ["-Dtests=false", "-Dgtkdoc=false"]
hostmakedepends = ["pkgconf", "meson", "cmake", "gobject-introspection"]
makedepends = ["xz-devel", "zstd-devel"]
checkdepends = ["shared-mime-info"]
depends = ["shared-mime-info"]
pkgdesc = "Library to help create and query binary XML blobs"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libxmlb"
source = f"https://github.com/hughsie/libxmlb/releases/download/{pkgver}/libxmlb-{pkgver}.tar.xz"
sha256 = "4cf605965d0e669db737da6443314664ea471807f2719a84550f2490670beea9"
options = ["!cross"]


@subpackage("libxmlb-devel")
def _devel(self):
    return self.default_devel()
