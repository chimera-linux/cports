pkgname = "libxmlb"
pkgver = "0.3.11"
pkgrel = 0
build_style = "meson"
# tests require some file to exist in /tmp? so it fails
configure_args = ["-Dtests=false", "-Dgtkdoc=false"]
hostmakedepends = [
    "pkgconf", "meson", "cmake", "gobject-introspection"
]
makedepends = ["liblzma-devel", "libzstd-devel"]
pkgdesc = "Library to help create and query binary XML blobs"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libxmlb"
source = f"https://github.com/hughsie/libxmlb/releases/download/{pkgver}/libxmlb-{pkgver}.tar.xz"
sha256 = "0bf704ca040b9ab371a62182d0d6417fe7ae38428e5f48846b87b99e74fe7c23"
options = ["!cross"]

@subpackage("libxmlb-devel")
def _devel(self):
  return self.default_devel()
