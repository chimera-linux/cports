pkgname = "at-spi2-core"
pkgver = "2.48.4"
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
sha256 = "29ecb12992e8339675f5d755c8735ea3ea298379cfa2c93fde96bee5dc57a515"
# non-trivial dbus setup
options = ["!check", "!cross"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


@subpackage("at-spi2-core-devel")
def _devel(self):
    return self.default_devel()
