pkgname = "wpebackend-fdo"
pkgver = "1.16.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["glib-devel", "libepoxy-devel", "libwpe-devel", "wayland-devel"]
pkgdesc = "Wayland backend for WPE WebKit"
license = "BSD-2-Clause"
url = "https://wpewebkit.org"
source = f"{url}/releases/wpebackend-fdo-{pkgver}.tar.xz"
sha256 = "544ae14012f8e7e426b8cb522eb0aaaac831ad7c35601d1cf31d37670e0ebb3b"


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
