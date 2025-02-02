pkgname = "libxmlb"
pkgver = "0.3.21"
pkgrel = 1
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
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libxmlb"
source = f"https://github.com/hughsie/libxmlb/releases/download/{pkgver}/libxmlb-{pkgver}.tar.xz"
sha256 = "642343c9b3eca5c234ef83d3d5f6307c78d024f2545f3cc2fa252c9e14e4efd1"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/installed-tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("libxmlb-devel")
def _(self):
    return self.default_devel()
