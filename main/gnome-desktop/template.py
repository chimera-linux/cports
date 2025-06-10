pkgname = "gnome-desktop"
pkgver = "44.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dudev=enabled",
    "-Dsystemd=disabled",
]
hostmakedepends = [
    "docbook-xml",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "fontconfig-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "iso-codes",
    "libseccomp-devel",
    "libxkbcommon-devel",
    "udev-devel",
    "xkeyboard-config",
]
depends = [
    "bubblewrap",
    "gsettings-desktop-schemas",
    "iso-codes",
    "xkeyboard-config",
]
pkgdesc = "GNOME desktop management utilities"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-desktop"
source = (
    f"$(GNOME_SITE)/gnome-desktop/{pkgver[:-2]}/gnome-desktop-{pkgver}.tar.xz"
)
sha256 = "40efa9aa8d50effed9227a3d70671e32e9dc35e20f331cab3b562975978f4f8d"
# needs graphical environment
options = ["!check", "!cross"]


@subpackage("gnome-desktop-devel")
def _(self):
    return self.default_devel()
