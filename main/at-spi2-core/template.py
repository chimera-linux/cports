pkgname = "at-spi2-core"
pkgver = "2.56.3"
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
sha256 = "0e41e1fc6a1961b38b4f9c0bea64bad30efff75949b7cdb988d2f2fdab72267a"
# non-trivial dbus setup
options = ["!check", "!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("at-spi2-core-devel")
def _(self):
    return self.default_devel()
