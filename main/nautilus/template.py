pkgname = "nautilus"
pkgver = "47_rc"
pkgrel = 0
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
depends = ["desktop-file-utils", "tinysparql", "localsearch"]
checkdepends = ["dbus", "tinysparql", "localsearch", "python-gobject"]
pkgdesc = "GNOME file manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Files"
source = f"$(GNOME_SITE)/nautilus/{pkgver[:2]}/nautilus-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "18d96f0ace33a5545b2f371afbeeaf00baea87ed9a72f7e26f300a59ba5df44a"
options = ["!cross"]


@subpackage("nautilus-devel")
def _(self):
    return self.default_devel()


@subpackage("nautilus-libs")
def _(self):
    return self.default_libs()
