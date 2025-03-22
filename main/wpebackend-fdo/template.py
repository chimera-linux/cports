pkgname = "wpebackend-fdo"
pkgver = "1.16.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["glib-devel", "libepoxy-devel", "libwpe-devel", "wayland-devel"]
pkgdesc = "Wayland backend for WPE WebKit"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/wpebackend-fdo-{pkgver}.tar.xz"
sha256 = "beddf321232d5bd08106c179dbc600f8ce88eb3620b4a59a6329063b78f64635"


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
