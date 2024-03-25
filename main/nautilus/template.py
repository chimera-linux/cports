pkgname = "nautilus"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtests=headless"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "gobject-introspection",
    "cmake",
    "desktop-file-utils",
]
makedepends = [
    "glib-devel",
    "gnome-desktop-devel",
    "gnome-autoar-devel",
    "libadwaita-devel",
    "gtk4-devel",
    "libportal-devel",
    "tracker-devel",
    "libxml2-devel",
    "gexiv2-devel",
    "gst-plugins-base-devel",
    "libcloudproviders-devel",
]
depends = ["desktop-file-utils", "tracker", "tracker-miners"]
checkdepends = ["dbus", "tracker", "tracker-miners", "python-gobject"]
pkgdesc = "GNOME file manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Files"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:pkgver.find('.')]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e6d75ed9f7aa68a00a2a559a0bf7010c6077e158d2d900fa365a8973f6ef11ce"
options = ["!cross"]


@subpackage("nautilus-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nautilus-libs")
def _libs(self):
    return self.default_libs()
