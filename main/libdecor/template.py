pkgname = "libdecor"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddemo=false", "-Ddbus=enabled",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "wayland-devel", "wayland-protocols", "pango-devel", "dbus-devel",
    "linux-headers",
]
pkgdesc = "Decorations library for Wayland clients"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.gnome.org/jadahl/libdecor"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1d5758cb49dcb9ceaa979ad14ceb6cdf39282af5ce12ebe6073dd193d6b2fb5e"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libdecor-devel")
def _devel(self):
    return self.default_devel()
