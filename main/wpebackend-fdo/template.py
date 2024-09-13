pkgname = "wpebackend-fdo"
pkgver = "1.14.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["glib-devel", "libepoxy-devel", "libwpe-devel", "wayland-devel"]
pkgdesc = "Wayland backend for WPE WebKit"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/wpebackend-fdo-{pkgver}.tar.xz"
sha256 = "10121842595a850291db3e82f3db0b9984df079022d386ce42c2b8508159dc6c"


def post_install(self):
    self.install_license("COPYING")


@subpackage("wpebackend-fdo-devel")
def _(self):
    self.depends += [self.parent]
    # does not include the .so file; it's dlopened by things at runtime
    return [
        "usr/include",
        "usr/lib/pkgconfig",
    ]
