pkgname = "libfprint"
pkgver = "1.94.8"
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
sha256 = "bf6a224bde98801de8615f76bcc0a4950b65a106b321b2cfccac9b679c241364"
# meson error: "ERROR: An exe_wrapper is needed but was not found."
options = ["!cross"]


@subpackage("libfprint-devel")
def _(self):
    return self.default_devel()
