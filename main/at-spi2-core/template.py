pkgname = "at-spi2-core"
pkgver = "2.53.90"
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
source = f"$(GNOME_SITE)/at-spi2-core/{pkgver[:4]}/at-spi2-core-{pkgver}.tar.xz"
sha256 = "0548e8dfc77b0a190827c767264a0b725311ab3af96588d52cadbab35e05c6aa"
# non-trivial dbus setup
options = ["!check", "!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("at-spi2-core-devel")
def _(self):
    return self.default_devel()
