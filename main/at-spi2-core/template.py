pkgname = "at-spi2-core"
pkgver = "2.42.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny",
    "gobject-introspection", "dbus"
]
makedepends = [
    "libglib-devel", "libxext-devel", "libxtst-devel",
    "libsm-devel", "dbus-devel"
]
pkgdesc = "Assistive Technology Service Provider Interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/at-spi2-core"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4b5da10e94fa3c6195f95222438f63a0234b99ef9df772c7640e82baeaa6e386"
# non-trivial dbus setup
options = ["!check"]

def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive = True)

@subpackage("at-spi2-core-devel")
def _devel(self):
    return self.default_devel()
