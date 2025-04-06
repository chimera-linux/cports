pkgname = "bluez"
pkgver = "5.82"
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
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
sha256 = "0739fa608a837967ee6d5572b43fb89946a938d1c6c26127158aaefd743a790b"
tool_flags = {
    "CFLAGS": ["-Wno-deprecated-declarations"],
    # workaround for --gc-sections breaking in test files
    "LDFLAGS": ["-Wl,-z,nostart-stop-gc"],
}


def post_install(self):
    self.install_service(self.files_path / "bluetoothd")


@subpackage("bluez-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libbluetooth")]

    return self.default_libs()


@subpackage("bluez-devel")
def _(self):
    return self.default_devel()


@subpackage("bluez-cups")
def _(self):
    self.pkgdesc = "CUPS printer backend for Bluetooth printers"
    self.install_if = [self.parent, "cups"]

    return ["usr/lib/cups/backend/bluetooth"]
