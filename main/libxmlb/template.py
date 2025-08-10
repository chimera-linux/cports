pkgname = "libxmlb"
pkgver = "0.3.23"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgtkdoc=false",
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = ["pkgconf", "meson", "gobject-introspection"]
makedepends = ["xz-devel", "zstd-devel"]
checkdepends = ["shared-mime-info"]
depends = ["shared-mime-info"]
pkgdesc = "Library to help create and query binary XML blobs"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libxmlb"
source = f"https://github.com/hughsie/libxmlb/releases/download/{pkgver}/libxmlb-{pkgver}.tar.xz"
sha256 = "ab86eb2073592448a4e0263ab56e222de092c0a3964b66a8d696cac071c8ee3c"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/installed-tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("libxmlb-devel")
def _(self):
    return self.default_devel()
