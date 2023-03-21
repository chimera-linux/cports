pkgname = "libical"
pkgver = "3.0.16"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DICAL_BUILD_DOCS=false", "-DGOBJECT_INTROSPECTION=true",
    "-DICAL_GLIB_VAPI=true",
]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "gettext-tiny", "glib-devel",
    "libxml2-devel", "perl", "vala", "gobject-introspection"
]
makedepends = [
    "glib-devel", "libxml2-devel", "vala-devel", "icu-devel",
]
checkdepends = ["python-gobject"]
pkgdesc = "Open source implementation of iCalendar protocols and formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-2.1-only"
url = "https://libical.github.io/libical"
source = f"https://github.com/{pkgname}/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "b44705dd71ca4538c86fb16248483ab4b48978524fb1da5097bd76aa2e0f0c33"
options = ["!cross"]

@subpackage("libical-devel")
def _devel(self):
    return self.default_devel()

def do_check(self):
    self.do(
        "ctest", "-E", "(icalrecurtest|icalrecurtest_r)", wrksrc = "build",
        env = {"CTEST_OUTPUT_ON_FAILURE": "TRUE"}
    )
