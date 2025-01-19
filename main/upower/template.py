pkgname = "upower"
pkgver = "1.90.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dos_backend=linux",
    "-Dsystemdsystemunitdir=no",
    "-Dintrospection=enabled",
    "-Dgtk-doc=false",
]
make_check_args = ["--timeout-multiplier", "2"]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "glib-devel",
    "libgudev-devel",
    "libimobiledevice-devel",
    "libusb-devel",
    "linux-headers",
]
checkdepends = [
    "dbus",
    "python-dbus",
    "python-dbusmock",
    "python-gobject",
    "python-packaging",
    "umockdev",
]
pkgdesc = "Abstraction for enumerating power devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://upower.freedesktop.org"
source = f"https://gitlab.freedesktop.org/upower/upower/-/archive/v{pkgver}/upower-v{pkgver}.tar.gz"
sha256 = "7d616e529ddfd4a4ced9dcf701c1d77628ef12e242d0603f32bedfa1a2c7e3ed"
options = ["!cross"]


@subpackage("upower-devel")
def _(self):
    return self.default_devel()


@subpackage("upower-libs")
def _(self):
    return self.default_libs()
