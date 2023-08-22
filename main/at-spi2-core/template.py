pkgname = "at-spi2-core"
pkgver = "2.48.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "gobject-introspection",
    "dbus",
]
makedepends = [
    "glib-devel",
    "libxext-devel",
    "libxtst-devel",
    "libsm-devel",
    "dbus-devel",
    "libxml2-devel",
]
pkgdesc = "Assistive Technology Service Provider Interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/at-spi2-core"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "37316df43ca9989ce539d54cf429a768c28bb38a0b34950beadd0421827edf55"
# non-trivial dbus setup
options = ["!check", "!cross"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


@subpackage("at-spi2-core-devel")
def _devel(self):
    return self.default_devel()
