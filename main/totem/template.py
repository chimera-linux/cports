pkgname = "totem"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-python=no",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
    "gettext-tiny", "itstool", "gstreamer", "gst-plugins-base",
    "gst-plugins-good",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "libhandy-devel", "gstreamer-devel",
    "gst-plugins-base-devel", "gst-plugins-good", "libpeas-devel",
    "totem-pl-parser-devel", "gsettings-desktop-schemas-devel",
    "gnome-desktop-devel", "grilo-devel",
]
# TODO: add grilo-plugins once we have them
depends = ["gst-plugins-good", "gst-libav", "gsettings-desktop-schemas"]
pkgdesc = "GNOME media player"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Videos"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4af0491ddb95df8b33aee399d3a50f9c7ab17de88d3af63356567cf88f57e6ab"
# needs graphical environment
options = ["!check"]

@subpackage("totem-libs")
def _libs(self):
    return self.default_libs()

@subpackage("totem-devel")
def _devel(self):
    return self.default_devel()
