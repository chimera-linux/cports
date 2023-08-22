pkgname = "nautilus"
pkgver = "44.2.1"
pkgrel = 1
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-4]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d9c62f024727f7a76fc6a5da788a2b0247df01a71c2a601143c62aac0ff41e4c"
options = ["!cross"]


@subpackage("nautilus-devel")
def _devel(self):
    return self.default_devel()


@subpackage("nautilus-libs")
def _libs(self):
    return self.default_libs()
