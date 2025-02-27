pkgname = "libfprint"
pkgver = "1.94.9"
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
sha256 = "6398e7a28c91b3a16ff17e6a577c7a03692a5de509e8def817396f1120823ecf"
# meson error: "ERROR: An exe_wrapper is needed but was not found."
options = ["!cross"]


@subpackage("libfprint-devel")
def _(self):
    return self.default_devel()
