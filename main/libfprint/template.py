pkgname = "libfprint"
pkgver = "1.94.100"
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
    "openssl3-devel",
    "pixman-devel",
]
checkdepends = ["python-cairo"]
pkgdesc = "Library for fingerprint readers"
license = "LGPL-2.1-or-later"
url = "https://fprint.freedesktop.org"
source = f"https://gitlab.freedesktop.org/libfprint/libfprint/-/archive/v{pkgver}/libfprint-v{pkgver}.tar.gz"
sha256 = "edc90e02f330a7595ceaf37f2c6ec32ed43541347fe936d3273b0bb2524fd19c"
# meson error: "ERROR: An exe_wrapper is needed but was not found."
options = ["!cross"]


@subpackage("libfprint-devel")
def _(self):
    return self.default_devel()
