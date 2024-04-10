pkgname = "upower"
pkgver = "1.90.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dos_backend=linux",
    "-Dsystemdsystemunitdir=no",
    "-Dintrospection=enabled",
    "-Dgtk-doc=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "docbook-xsl-nons",
    "xsltproc",
]
makedepends = [
    "libusb-devel",
    "libgudev-devel",
    "glib-devel",
    "libimobiledevice-devel",
    "linux-headers",
]
checkdepends = ["python-packaging", "python-dbus", "python-gobject"]
pkgdesc = "Abstraction for enumerating power devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://upower.freedesktop.org"
source = f"https://gitlab.freedesktop.org/upower/upower/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "cd194dd278bd8d058b4728efd1d0a91cdf017378f025b558beb6f60a86af4781"
# unpackaged umockdev
options = ["!check"]


@subpackage("upower-devel")
def _devel(self):
    return self.default_devel()


@subpackage("upower-libs")
def _libs(self):
    return self.default_libs()
