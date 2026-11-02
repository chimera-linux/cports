pkgname = "at-spi2-core"
pkgver = "2.62.1"
pkgrel = 0
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
sha256 = "cca6b6a86e4389d89b370288761ce2385ddeceb10c4412da78689bc30c88af2d"
# non-trivial dbus setup
options = ["etcfiles", "!check", "!cross"]


@subpackage("at-spi2-core-devel")
def _(self):
    return self.default_devel()
