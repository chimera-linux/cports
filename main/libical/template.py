pkgname = "libical"
pkgver = "3.0.18"
pkgrel = 2
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-only"
url = "https://libical.github.io/libical"
source = f"https://github.com/libical/libical/archive/v{pkgver}.tar.gz"
sha256 = "72b7dc1a5937533aee5a2baefc990983b66b141dd80d43b51f80aced4aae219c"
options = ["!cross"]


@subpackage("libical-devel")
def _(self):
    return self.default_devel()
