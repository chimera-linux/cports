pkgname = "libical"
pkgver = "3.0.20"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DICAL_BUILD_DOCS=OFF",
    "-DGOBJECT_INTROSPECTION=ON",
    "-DICAL_GLIB_VAPI=ON",
    "-DLIBICAL_BUILD_EXAMPLES=OFF",
]
make_check_args = ["-E", "(icalrecurtest|icalrecurtest_r)"]
hostmakedepends = [
    "cmake",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxml2-devel",
    "ninja",
    "perl",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "icu-devel",
    "libxml2-devel",
    "vala-devel",
]
checkdepends = ["python-gobject"]
pkgdesc = "Open source implementation of iCalendar protocols and formats"
license = "MPL-2.0 OR LGPL-2.1-only"
url = "https://libical.github.io/libical"
source = f"https://github.com/libical/libical/archive/v{pkgver}.tar.gz"
sha256 = "e73de92f5a6ce84c1b00306446b290a2b08cdf0a80988eca0a2c9d5c3510b4c2"
options = ["!cross"]


@subpackage("libical-devel")
def _(self):
    return self.default_devel()
