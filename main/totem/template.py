pkgname = "totem"
pkgver = "43.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-python=no",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext",
    "itstool",
    "gstreamer",
    "gst-plugins-base",
    "gst-plugins-good",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "gst-plugins-good",
    "libpeas-devel",
    "totem-pl-parser-devel",
    "gsettings-desktop-schemas-devel",
    "gnome-desktop-devel",
    "grilo-devel",
]
depends = [
    "grilo-plugins",
    "gst-plugins-good",
    "gst-libav",
    "gsettings-desktop-schemas",
]
pkgdesc = "GNOME media player"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Videos"
source = f"$(GNOME_SITE)/totem/{pkgver[:-2]}/totem-{pkgver}.tar.xz"
sha256 = "5668291e9c6444985cb3ffe4ea4f0212f54c2bbe60dd01114c1a950f94759e6d"
# needs graphical environment
options = ["!check"]


@subpackage("totem-libs")
def _(self):
    return self.default_libs()


@subpackage("totem-devel")
def _(self):
    return self.default_devel()
