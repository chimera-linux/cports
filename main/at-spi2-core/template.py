pkgname = "at-spi2-core"
pkgver = "2.60.3"
pkgrel = 1
build_style = "meson"
configure_args = [
    # needs dbus-broker fix in the future
    "-Duse_systemd=false",
    "-Dgtk2_atk_adaptor=false",
]
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
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/at-spi2-core"
source = (
    f"$(GNOME_SITE)/at-spi2-core/{pkgver[:-2]}/at-spi2-core-{pkgver}.tar.xz"
)
sha256 = "21056bc04e43e8ed34fdafd916a0ddcc29ec03a4ce6cf5aacac1ddf6ef185ef7"
# non-trivial dbus setup
options = ["!check", "!cross"]


@subpackage("at-spi2-core-devel")
def _(self):
    return self.default_devel()
