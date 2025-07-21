pkgname = "clapper"
pkgver = "0.8.0"
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
sha256 = "f0d6faea1285ff4b3a1c3c758181cd1b501cd066f87afd0d6fde5fc7e83eba60"
# FIXME: clapper gst upload plugin has a needed on libgstclapper.so in here, and
# it fails to load without explicit rpath
tool_flags = {"LDFLAGS": ["-Wl,--rpath=/usr/lib/gstreamer-1.0"]}
# gobject-introspection
options = ["!cross"]


@subpackage("clapper-devel")
def _(self):
    return self.default_devel()
