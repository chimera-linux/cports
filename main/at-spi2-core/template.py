pkgname = "at-spi2-core"
pkgver = "2.44.0"
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
sha256 = "7eee3cf285b089060fd6b6e51b3eb2cacf752cca3a082c7f4c2c5ab841e51353"
# non-trivial dbus setup
options = ["!check", "!cross"]

def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive = True)

@subpackage("at-spi2-core-devel")
def _devel(self):
    return self.default_devel()
