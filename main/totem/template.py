pkgname = "totem"
pkgver = "43.2"
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
license = "GPL-2.0-or-later"
url = "https://apps.gnome.org/Totem"
source = f"$(GNOME_SITE)/totem/{pkgver[:-2]}/totem-{pkgver}.tar.xz"
sha256 = "0b007d30fbb93b95a604f14848a497f57fc333a75c2e638a249972e99c01e6a4"
# needs graphical environment
options = ["!check"]


@subpackage("totem-libs")
def _(self):
    return self.default_libs()


@subpackage("totem-devel")
def _(self):
    return self.default_devel()
