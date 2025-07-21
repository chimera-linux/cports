pkgname = "upower"
pkgver = "1.90.9"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
sha256 = "fffd45c50d29ed73ecdcfb11c3a7bb042ef14e84b14b0c2d5fdb78c7b4435d6c"
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
