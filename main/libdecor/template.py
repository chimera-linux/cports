pkgname = "libdecor"
pkgver = "0.2.4"
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
sha256 = "1fb3ee6c7c9e238d240772517753bedb2e09e29d21514fb86f19724fccb58cc1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdecor-devel")
def _(self):
    return self.default_devel()
