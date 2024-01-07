pkgname = "totem"
pkgver = "43.0"
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
# TODO: add grilo-plugins once we have them
depends = ["gst-plugins-good", "gst-libav", "gsettings-desktop-schemas"]
pkgdesc = "GNOME media player"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Videos"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b36d3655928b5896462a4d39f83b6ad66d37dbc9c99dceb02ea8a2e37394a41e"
# needs graphical environment
options = ["!check"]


@subpackage("totem-libs")
def _libs(self):
    return self.default_libs()


@subpackage("totem-devel")
def _devel(self):
    return self.default_devel()
