pkgname = "libdecor"
pkgver = "0.1.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddemo=false",
    "-Ddbus=enabled",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "wayland-devel",
    "wayland-protocols",
    "pango-devel",
    "dbus-devel",
    "linux-headers",
]
pkgdesc = "Decorations library for Wayland clients"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.gnome.org/jadahl/libdecor"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "82adece5baeb6194292b0d1a91b4b3d10da41115f352a5e6c5844b20b88a0512"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdecor-devel")
def _devel(self):
    return self.default_devel()
