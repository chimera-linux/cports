pkgname = "at-spi2-core"
pkgver = "2.50.1"
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
sha256 = "5727b5c0687ac57ba8040e79bd6731b714a36b8fcf32190f236b8fb3698789e7"
# non-trivial dbus setup
options = ["!check", "!cross"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


@subpackage("at-spi2-core-devel")
def _devel(self):
    return self.default_devel()
