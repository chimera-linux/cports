pkgname = "python-dbus"
pkgver = "1.3.2"
pkgrel = 3
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "python-devel"]
makedepends = ["glib-devel", "dbus-devel", "python-devel"]
checkdepends = ["dbus"]
depends = ["python"]
pkgdesc = "Python bindings for D-Bus"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/DBusBindings"
source = f"https://dbus.freedesktop.org/releases/dbus-python/dbus-python-{pkgver}.tar.gz"
sha256 = "ad67819308618b5069537be237f8e68ca1c7fcc95ee4a121fe6845b1418248f8"


def post_install(self):
    self.install_license("COPYING")


@subpackage("python-dbus-devel")
def _(self):
    self.depends += [self.parent, "python-devel"]

    return self.default_devel()
