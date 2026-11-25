pkgname = "bluez"
pkgver = "5.88"
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
sha256 = "6952c39eb5f8b0ee712cc50ab3bcff03be17c410dd97ca640f4849d9a1653ba3"
tool_flags = {
    "CFLAGS": ["-Wno-deprecated-declarations"],
    # workaround for --gc-sections breaking in test files
    "LDFLAGS": ["-Wl,-z,nostart-stop-gc"],
}
options = ["etcfiles"]


def post_install(self):
    self.install_service(self.files_path / "bluetoothd")
    self.install_service(self.files_path / "mpris-proxy.user")


@split("libs")
def _(self):
    self.renames = ["libbluetooth"]

    return self.default_libs()


@split("devel")
def _(self):
    return self.default_devel()


@split("cups")
def _(self):
    self.pkgdesc = "CUPS printer backend for Bluetooth printers"
    self.install_if = [self.parent, "cups"]

    return ["usr/lib/cups/backend/bluetooth"]
