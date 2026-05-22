pkgname = "upower"
pkgver = "1.91.2"
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
    "libxslt-progs",
    "meson",
    "pkgconf",
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
license = "GPL-2.0-or-later"
url = "https://upower.freedesktop.org"
source = f"https://gitlab.freedesktop.org/upower/upower/-/archive/v{pkgver}/upower-v{pkgver}.tar.gz"
sha256 = "cd9a3a3f5e0aa21eac131253228757bbdc90ecd39768f46c325754e32daa3083"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/upower/integration-test.py")
    self.uninstall("usr/lib/upower/output_checker.py")
    self.uninstall("usr/lib/upower/tests")
    self.uninstall("usr/share/installed-tests")


@subpackage("upower-devel")
def _(self):
    return self.default_devel()


@subpackage("upower-libs")
def _(self):
    return self.default_libs()
