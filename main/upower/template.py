pkgname = "upower"
pkgver = "1.90.4"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dos_backend=linux",
    "-Dsystemdsystemunitdir=no",
    "-Dintrospection=enabled",
    "-Dgtk-doc=false",
]
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
sha256 = "cd194dd278bd8d058b4728efd1d0a91cdf017378f025b558beb6f60a86af4781"
options = ["!cross"]


@subpackage("upower-devel")
def _(self):
    return self.default_devel()


@subpackage("upower-libs")
def _(self):
    return self.default_libs()
