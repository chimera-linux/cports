pkgname = "at-spi2-core"
pkgver = "2.54.0"
pkgrel = 1
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/at-spi2-core"
source = (
    f"$(GNOME_SITE)/at-spi2-core/{pkgver[:-2]}/at-spi2-core-{pkgver}.tar.xz"
)
sha256 = "d7eee7e75beddcc272cedc2b60535600f3aae6e481589ebc667afc437c0a6079"
# non-trivial dbus setup
options = ["!check", "!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("at-spi2-core-devel")
def _(self):
    return self.default_devel()
