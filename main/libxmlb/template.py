pkgname = "libxmlb"
pkgver = "0.3.14"
pkgrel = 1
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
sha256 = "a2f0056eed14ff791aee2b08b1514a0f1b6cf215f0579138a8cae8c45a0d3b0f"
options = ["!cross"]


@subpackage("libxmlb-devel")
def _devel(self):
    return self.default_devel()
