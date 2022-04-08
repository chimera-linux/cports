pkgname = "libical"
pkgver = "3.0.14"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DICAL_BUILD_DOCS=false", "-DGOBJECT_INTROSPECTION=true",
    "-DICAL_GLIB_VAPI=true",
]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "gettext-tiny", "libglib-devel",
    "libxml2-devel", "perl", "vala", "gobject-introspection"
]
makedepends = [
    "libglib-devel", "libxml2-devel", "vala-devel", "icu-devel",
]
checkdepends = ["python-gobject"]
pkgdesc = "Open source implementation of iCalendar protocols and formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-only"
url = "https://libical.github.io/libical"
source = f"https://github.com/{pkgname}/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "4284b780356f1dc6a01f16083e7b836e63d3815e27ed0eaaad684712357ccc8f"
options = ["!cross"]

@subpackage("libical-devel")
def _devel(self):
    return self.default_devel()
