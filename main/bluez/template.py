pkgname = "bluez"
pkgver = "5.75"
pkgrel = 1
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
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "flex",
    "gmake",
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
pkgdesc = "Linux Bluetooth stack"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/{pkgname}-{pkgver}.tar.xz"
sha256 = "988cb3c4551f6e3a667708a578f5ca9f93fc896508f98f08709be4f8ab033c2f"
tool_flags = {
    "CFLAGS": ["-Wno-deprecated-declarations"],
    # workaround for --gc-sections breaking in test files
    "LDFLAGS": ["-Wl,-z,nostart-stop-gc"],
}


def post_install(self):
    self.install_service(self.files_path / "bluetoothd")


@subpackage("libbluetooth")
def _libs(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("bluez-devel")
def _devel(self):
    return self.default_devel()


@subpackage("bluez-cups")
def _cups(self):
    self.pkgdesc = "CUPS printer backend for Bluetooth printers"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "cups"]

    return ["usr/lib/cups/backend/bluetooth"]
