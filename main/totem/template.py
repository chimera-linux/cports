pkgname = "totem"
pkgver = "41_alpha0"
# use a snapshot for now to avoid clutter-gtk
_commit = "b0cd071c7cbc85aaa8ff0cde02b821084d6eedda"
_libgd = "cc90107531640bcba6c3c58e5cf6aec94d498763"
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
source = [
    f"https://gitlab.gnome.org/GNOME/{pkgname}/-/archive/{_commit}.tar.gz",
    f"https://gitlab.gnome.org/GNOME/libgd/-/archive/{_libgd}.tar.gz",
]
sha256 = [
    "d069e2d8e38016bd3248dd8a7cb2dffc8eb08c9f5b5eee2d0acb11cb60112ec5",
    "f068de749a30695cd361fa6406c71421caf66f976008e7385dcd80fead6f46ad",
]
# needs graphical environment
options = ["!check"]

def post_extract(self):
    for f in (self.cwd / f"totem-{_commit}").iterdir():
        self.mv(f, ".")
    self.rm("subprojects/libgd", recursive = True)
    self.mv(f"libgd-{_libgd}", "subprojects/libgd")

@subpackage("totem-libs")
def _libs(self):
    return self.default_libs()

@subpackage("totem-devel")
def _devel(self):
    return self.default_devel()
