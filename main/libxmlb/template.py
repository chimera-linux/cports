pkgname = "libxmlb"
pkgver = "0.3.16"
pkgrel = 0
build_style = "meson"
# tests require some file to exist in /tmp? so it fails
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
sha256 = "8007d39eefaa047d23e323523ae3c4da5fca77543b0fc4e188f7a3cd28872ff4"
options = ["!cross"]


@subpackage("libxmlb-devel")
def _devel(self):
    return self.default_devel()
