pkgname = "python-dbus"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "libtool",
    "pkgconf",
    "python-devel",
]
makedepends = ["glib-devel", "dbus-devel", "python-devel"]
checkdepends = ["dbus"]
depends = ["python"]
pkgdesc = "Python bindings for D-Bus"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/DBusBindings"
source = f"https://dbus.freedesktop.org/releases/dbus-python/dbus-python-{pkgver}.tar.xz"
sha256 = "c36b28f10ffcc8f1f798aca973bcc132f91f33eb9b6b8904381b4077766043d5"


def post_install(self):
    self.install_license("COPYING")


@subpackage("python-dbus-devel")
def _(self):
    self.depends += [self.parent, "python-devel"]

    return self.default_devel()
