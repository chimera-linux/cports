pkgname = "nautilus"
pkgver = "49.1"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dtests=headless"]
hostmakedepends = [
    "cmake",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "gexiv2-devel",
    "glib-devel",
    "gnome-autoar-devel",
    "gnome-desktop-devel",
    "gst-plugins-base-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libcloudproviders-devel",
    "libportal-devel",
    "libxml2-devel",
    "tinysparql-devel",
]
depends = ["desktop-file-utils", "localsearch", "tinysparql"]
checkdepends = ["dbus", "localsearch", "tinysparql", "python-gobject"]
pkgdesc = "GNOME file manager"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Files"
source = f"$(GNOME_SITE)/nautilus/{pkgver[: pkgver.find('.')]}/nautilus-{pkgver}.tar.xz"
sha256 = "add2a0e410fd22da2851ddd0c5b3d22c9e9d8c33111511f336961e3b461b535e"
# introspection
options = ["!cross"]


@subpackage("nautilus-devel")
def _(self):
    return self.default_devel()


@subpackage("nautilus-libs")
def _(self):
    return self.default_libs()
