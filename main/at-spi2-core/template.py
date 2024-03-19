pkgname = "at-spi2-core"
pkgver = "2.50.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "dbus",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "libsm-devel",
    "libxext-devel",
    "libxml2-devel",
    "libxtst-devel",
]
pkgdesc = "Assistive Technology Service Provider Interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/at-spi2-core"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5b81b1461a62dd8fbed1a276fa9ef5b7112f9ae5ff86e1e32ad9644b654ff78c"
# non-trivial dbus setup
options = ["!check", "!cross"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


@subpackage("at-spi2-core-devel")
def _devel(self):
    return self.default_devel()
