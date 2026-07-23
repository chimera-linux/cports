pkgname = "at-spi2-core"
pkgver = "2.60.5"
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
sha256 = "6059a77d507438ff6c8d6d06025f8f9f5774fa0f8eabe9c9b059b1cc41e1bbc0"
# non-trivial dbus setup
options = ["etcfiles", "!check", "!cross"]


@subpackage("at-spi2-core-devel")
def _(self):
    return self.default_devel()
