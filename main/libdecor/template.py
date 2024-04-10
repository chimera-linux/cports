pkgname = "libdecor"
pkgver = "0.2.2"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/libdecor/libdecor"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "40a1d8be07d8b1f66e8fb98a1f4a84549ca6bf992407198a5055952be80a8525"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdecor-devel")
def _devel(self):
    return self.default_devel()
