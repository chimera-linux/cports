pkgname = "clapper"
pkgver = "0.6.1"
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
    "gst-plugins-base-devel",
    "glib-devel",
    "gstreamer-devel",
    "libadwaita-devel",
    "libmicrodns-devel",
    "libsoup-devel",
]
pkgdesc = "Simple media player"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://rafostar.github.io/clapper"
source = (
    f"https://github.com/Rafostar/clapper/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "d244ec6108ebff5ccc817a5888f3f73f52cac129fe480d480cb3f6b9db19cfbe"
# FIXME: clapper gst upload plugin has a needed on libgstclapper.so in here, and
# it fails to load without explicit rpath
tool_flags = {"LDFLAGS": ["-Wl,--rpath=/usr/lib/gstreamer-1.0"]}
# gobject-introspection
options = ["!cross"]


@subpackage("clapper-devel")
def _(self):
    return self.default_devel()
