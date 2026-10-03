pkgname = "libical"
pkgver = "4.0.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIBICAL_BUILD_DOCS=OFF",
    "-DLIBICAL_BUILD_EXAMPLES=OFF",
    "-DLIBICAL_GLIB_VAPI=ON",
    "-DLIBICAL_GOBJECT_INTROSPECTION=ON",
    "-DLIBICAL_JAVA_BINDINGS=OFF",
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
sha256 = "cc09a3ac41d60e6144e644bd3fcf97d47106d659c4a0b8965102581401e67c9c"
options = ["!cross"]


@subpackage("libical-devel")
def _(self):
    return self.default_devel()
