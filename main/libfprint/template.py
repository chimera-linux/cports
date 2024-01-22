pkgname = "libfprint"
pkgver = "1.94.7"
pkgrel = 0
build_style = "meson"
# Needs virtual drivers (`-Ddrivers=all`) to run all tests, but they fail and I
# haven't figured out how to fix them
configure_args = ["-Dinstalled-tests=false", "-Ddoc=false"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    # Actually a checkdepends but the package checks for it regardless
    "python-gobject",
]
makedepends = [
    "glib-devel",
    "libgudev-devel",
    "libgusb-devel",
    "linux-headers",
    "nss-devel",
    "pixman-devel",
]
checkdepends = ["python-cairo"]
pkgdesc = "Library for fingerprint readers"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://fprint.freedesktop.org"
source = f"https://gitlab.freedesktop.org/libfprint/libfprint/-/archive/v{pkgver}/libfprint-v{pkgver}.tar.gz"
sha256 = "6d2cc09c72f86865b49a911690b43e363aed7595b66e6599232a572ccce95342"


@subpackage("libfprint-devel")
def _devel(self):
    return self.default_devel()
