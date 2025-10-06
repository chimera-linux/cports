pkgname = "at-spi2-core"
pkgver = "2.58.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
sha256 = "dfdd3300da2783a21969ffade2889817fb7c1906a4ef92497eba65969b3dab5a"
# non-trivial dbus setup
options = ["!check", "!cross"]


@subpackage("at-spi2-core-devel")
def _(self):
    return self.default_devel()
