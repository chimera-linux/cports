pkgname = "gstreamer"
pkgver = "1.20.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dptp-helper-permissions=capabilities",
    "-Dpackage-origin=https://chimera-linux.org",
    "-Ddbghelp=disabled",
    "-Dintrospection=enabled",
    "-Ddefault_library=shared",
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "flex", "python", "docbook-xsl-nons",
    "bison", "glib-devel", "libcap-progs", "gobject-introspection",
]
makedepends = [
    "libxml2-devel", "libglib-devel", "libcap-devel", "bash-completion",
]
pkgdesc = "Core GStreamer libraries and elements"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "67c1edf8c3c339cda5dde85f4f7b953bb9607c2d13ae970e2491c5c4c055ef5f"
options = ["!cross"]

@subpackage("gstreamer-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/share/gdb", "usr/share/gstreamer-1.0"
    ])
