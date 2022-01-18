pkgname = "upower"
pkgver = "0.99.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--with-backend=linux", "--enable-introspection",
    "--without-idevice", # FIXME
]
configure_env = {"MAKE": "gmake"}
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "gettext-tiny-devel", "glib-devel", "gtk-doc-tools",
    "gobject-introspection", "xsltproc",
]
makedepends = [
    "libusb-devel", "libgudev-devel", "libglib-devel", "linux-headers",
]
checkdepends = ["python-packaging", "python-dbus"]
pkgdesc = "Abstraction for enumerating power devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://upower.freedesktop.org"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/uploads/177df5b9f9b76f25a2ad9da41aa0c1fa/{pkgname}-{pkgver}.tar.xz"
sha256 = "5cad70f91540cc7dc121cb17e0ad645e5e663c8682f60a7be42ee38cd7b23d7a"
# unpackaged python-dbus
options = ["!check"]

@subpackage("upower-devel")
def _devel(self):
    return self.default_devel()

@subpackage("upower-libs")
def _libs(self):
    return self.default_libs()
