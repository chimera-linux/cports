pkgname = "nautilus"
pkgver = "42.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtests=headless"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "gobject-introspection",
    "cmake",
]
makedepends = [
    "libglib-devel", "gnome-desktop-devel", "gnome-autoar-devel",
    "libhandy-devel", "gtk+3-devel", "libportal-devel", "tracker-devel",
    "libxml2-devel", "gexiv2-devel", "gst-plugins-base-devel",
]
depends = ["hicolor-icon-theme", "tracker", "tracker-miners"]
checkdepends = ["dbus", "tracker", "tracker-miners", "python-gobject"]
pkgdesc = "GNOME file manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Files"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "99212d2eb75996f181728ad04a2e2d86f2577b064e68a34c8b81a7037df4ccb2"
options = ["!cross"]

@subpackage("nautilus-devel")
def _devel(self):
    return self.default_devel()

@subpackage("nautilus-libs")
def _libs(self):
    return self.default_libs()
