pkgname = "libical"
pkgver = "3.0.17"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DICAL_BUILD_DOCS=false",
    "-DGOBJECT_INTROSPECTION=true",
    "-DICAL_GLIB_VAPI=true",
]
make_check_args = ["-E", "(icalrecurtest|icalrecurtest_r)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "gettext",
    "glib-devel",
    "libxml2-devel",
    "perl",
    "vala",
    "gobject-introspection",
]
makedepends = [
    "glib-devel",
    "libxml2-devel",
    "vala-devel",
    "icu-devel",
]
checkdepends = ["python-gobject"]
pkgdesc = "Open source implementation of iCalendar protocols and formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-only"
url = "https://libical.github.io/libical"
source = f"https://github.com/libical/libical/archive/v{pkgver}.tar.gz"
sha256 = "bcda9a6db6870240328752854d1ea475af9bbc6356e6771018200e475e5f781b"
options = ["!cross"]


@subpackage("libical-devel")
def _devel(self):
    return self.default_devel()
