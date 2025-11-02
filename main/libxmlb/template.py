pkgname = "libxmlb"
pkgver = "0.3.24"
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
sha256 = "ded52667aac942bb1ff4d1e977e8274a9432d99033d86918feb82ade82b8e001"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/installed-tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("libxmlb-devel")
def _(self):
    return self.default_devel()
