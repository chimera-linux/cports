pkgname = "nautilus"
pkgver = "50.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dselinux=disabled", "-Dtests=headless"]
hostmakedepends = [
    "blueprint-compiler",
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
    "glycin-gtk4-devel",
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
sha256 = "d62793b9659771b66a6b6e052b52229f868ddbec1388a0b669eef0bd211212ee"
# introspection
options = ["!cross"]


@subpackage("nautilus-devel")
def _(self):
    return self.default_devel()


@subpackage("nautilus-libs")
def _(self):
    return self.default_libs()
