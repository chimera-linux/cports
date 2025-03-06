pkgname = "system-config-printer"
pkgver = "1.5.18"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "desktop-file-utils",
    "gettext-devel",
    "libxml2-progs",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "xmlto",
]
makedepends = ["cups-devel", "glib-devel", "libusb-devel", "udev-devel"]
depends = [
    "gdk-pixbuf",
    "gtk+3",
    "libhandy",
    "libnotify",
    "libsecret",
    "python-cairo",
    "python-dbus",
    "python-gobject",
    "python-pycups",
]
pkgdesc = "Graphical user interface for CUPS administration"
license = "GPL-2.0-or-later"
url = "https://github.com/OpenPrinting/system-config-printer"
source = (
    f"{url}/releases/download/v{pkgver}/system-config-printer-{pkgver}.tar.xz"
)
sha256 = "b1a69e1b4ec2add569a87aeca811a37c5361ee6ae327ec852b79e64223e34bee"


def post_install(self):
    self.rename(
        "etc/dbus-1/system.d", "usr/share/dbus-1/system.d", relative=False
    )
