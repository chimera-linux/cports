pkgname = "upower"
pkgver = "0.99.17"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared", "-Dos_backend=linux",
    "-Dsystemdsystemunitdir=no", "-Dintrospection=enabled", "-Dgtk-doc=false"
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny-devel", "glib-devel",
    "gobject-introspection", "docbook-xsl-nons", "xsltproc",
]
makedepends = [
    "libusb-devel", "libgudev-devel", "libglib-devel",
    "libimobiledevice-devel", "linux-headers",
]
checkdepends = ["python-packaging", "python-dbus", "python-gobject"]
pkgdesc = "Abstraction for enumerating power devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://upower.freedesktop.org"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "14d91e98aa3a8c298e314b2df371c3dbe3ed9a0dab74b43678c38b27a67d555d"
# unpackaged umockdev
options = ["!check"]

@subpackage("upower-devel")
def _devel(self):
    return self.default_devel()

@subpackage("upower-libs")
def _libs(self):
    return self.default_libs()
