pkgname = "clapper"
pkgver = "0.10.0"
pkgrel = 0
build_style = "meson"
# avoid .a gst
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "libadwaita-devel",
    "libmicrodns-devel",
    "libpeas2-devel",
    "libsoup-devel",
]
pkgdesc = "Simple media player"
license = "GPL-3.0-or-later"
url = "https://rafostar.github.io/clapper"
source = (
    f"https://github.com/Rafostar/clapper/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "344c0f20e540a63c6fb44cdd5de88c168ed145bb66c1307e79b2b08124780118"
# FIXME: clapper gst upload plugin has a needed on libgstclapper.so in here, and
# it fails to load without explicit rpath
tool_flags = {"LDFLAGS": ["-Wl,--rpath=/usr/lib/gstreamer-1.0"]}
# gobject-introspection
options = ["!cross"]


@subpackage("clapper-devel")
def _(self):
    return self.default_devel()
