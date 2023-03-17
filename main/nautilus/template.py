pkgname = "nautilus"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtests=headless"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "gobject-introspection",
    "cmake", "desktop-file-utils",
]
makedepends = [
    "libglib-devel", "gnome-desktop-devel", "gnome-autoar-devel",
    "libadwaita-devel", "gtk4-devel", "libportal-devel", "tracker-devel",
    "libxml2-devel", "gexiv2-devel", "gst-plugins-base-devel",
    "libcloudproviders-devel",
]
depends = ["hicolor-icon-theme", "tracker", "tracker-miners"]
checkdepends = ["dbus", "tracker", "tracker-miners", "python-gobject"]
pkgdesc = "GNOME file manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Files"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "57b99ebb8e2b9c1512d381e53096188c087b33410d6c52d87a27bd60ee76ac7f"
options = ["!cross"]

@subpackage("nautilus-devel")
def _devel(self):
    return self.default_devel()

@subpackage("nautilus-libs")
def _libs(self):
    return self.default_libs()
