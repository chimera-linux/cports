pkgname = "libxmlb"
pkgver = "0.3.20"
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
sha256 = "4c5b534d645f7328643d6a0d3040ffb9832e13e3530025af55086a06e3c018ed"
options = ["!cross"]


@subpackage("libxmlb-devel")
def _(self):
    return self.default_devel()
