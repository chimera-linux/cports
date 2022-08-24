pkgname = "at-spi2-core"
pkgver = "2.44.1"
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
sha256 = "4beb23270ba6cf7caf20b597354d75194d89afb69d2efcf15f4271688ba6f746"
# non-trivial dbus setup
options = ["!check", "!cross"]

def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive = True)

@subpackage("at-spi2-core-devel")
def _devel(self):
    return self.default_devel()
