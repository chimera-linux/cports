pkgname = "python-dbus"
pkgver = "1.3.2"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "python-devel"]
makedepends = ["glib-devel", "dbus-devel", "python-devel"]
checkdepends = ["dbus"]
depends = ["python", "dbus"]
pkgdesc = "Python bindings for D-Bus"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/DBusBindings"
source = f"https://dbus.freedesktop.org/releases/dbus-python/dbus-python-{pkgver}.tar.gz"
sha256 = "ad67819308618b5069537be237f8e68ca1c7fcc95ee4a121fe6845b1418248f8"


def post_install(self):
    self.install_license("COPYING")


@subpackage("python-dbus-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python-devel"]

    return self.default_devel()


configure_gen = []
