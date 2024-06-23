pkgname = "clapper"
pkgver = "0.6.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://rafostar.github.io/clapper"
source = (
    f"https://github.com/Rafostar/clapper/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "65cc76afe6fc11058855d98058b6f371e557ea4f29f2f6bf4e0178b6978585de"
# FIXME: clapper gst upload plugin has a needed on libgstclapper.so in here, and
# it fails to load without explicit rpath
tool_flags = {"LDFLAGS": ["-Wl,--rpath=/usr/lib/gstreamer-1.0"]}
# gobject-introspection
options = ["!cross"]


@subpackage("clapper-devel")
def _devel(self):
    return self.default_devel()
