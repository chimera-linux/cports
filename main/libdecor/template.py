pkgname = "libdecor"
pkgver = "0.2.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddemo=false",
    "-Ddbus=enabled",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "dbus-devel",
    "gtk+3-devel",
    "linux-headers",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Decorations library for Wayland clients"
license = "MIT"
url = "https://gitlab.freedesktop.org/libdecor/libdecor"
source = f"{url}/-/archive/{pkgver}/libdecor-{pkgver}.tar.gz"
sha256 = "21a471e3f48088d3fd8ecc5999c45258a32198782c0157482f7ebe82de42f79c"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdecor-devel")
def _(self):
    return self.default_devel()
