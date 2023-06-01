pkgname = "gstreamer"
pkgver = "1.22.3"
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
    "meson",
    "pkgconf",
    "gettext-tiny",
    "flex",
    "python",
    "docbook-xsl-nons",
    "bison",
    "glib-devel",
    "libcap-progs",
    "gobject-introspection",
]
makedepends = [
    "libxml2-devel",
    "glib-devel",
    "libcap-devel",
    "bash-completion",
]
pkgdesc = "Core GStreamer libraries and elements"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "9ffeab95053f9f6995eb3b3da225e88f21c129cd60da002d3f795db70d6d5974"
options = ["!cross"]


@subpackage("gstreamer-devel")
def _devel(self):
    return self.default_devel(
        extra=["usr/share/gdb", "usr/share/gstreamer-1.0"]
    )
