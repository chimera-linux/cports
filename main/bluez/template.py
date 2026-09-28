pkgname = "bluez"
pkgver = "5.87"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-deprecated",
    "--disable-experimental",
    "--disable-mesh",
    "--disable-nfc",
    "--disable-systemd",
    "--enable-cups",
    "--enable-library",
    "--enable-sixaxis",
    "--enable-threads",
    "--with-udevdir=/usr/lib/udev",
]
hostmakedepends = [
    "automake",
    "flex",
    "libtool",
    "pkgconf",
    "python-docutils",
]
# TODO: look into porting to libedit later
# same story as iwd, really crappy usage of readline API
makedepends = [
    "cups-devel",
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "glib-devel",
    "libical-devel",
    "linux-headers",
    "musl-bsd-headers",
    "readline-devel",
    "udev-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "Linux Bluetooth stack"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/bluez-{pkgver}.tar.xz"
sha256 = "26bdcf2cebd7310c6f598850606b037ef0c515fe6608ebc54d22c50c4c32b35f"
tool_flags = {
    "CFLAGS": ["-Wno-deprecated-declarations"],
    # workaround for --gc-sections breaking in test files
    "LDFLAGS": ["-Wl,-z,nostart-stop-gc"],
}
options = ["etcfiles"]


def post_install(self):
    self.install_service(self.files_path / "bluetoothd")
    self.install_service(self.files_path / "mpris-proxy.user")


@subpackage("bluez-libs")
def _(self):
    self.renames = ["libbluetooth"]

    return self.default_libs()


@subpackage("bluez-devel")
def _(self):
    return self.default_devel()


@subpackage("bluez-cups")
def _(self):
    self.pkgdesc = "CUPS printer backend for Bluetooth printers"
    self.install_if = [self.parent, "cups"]

    return ["usr/lib/cups/backend/bluetooth"]
