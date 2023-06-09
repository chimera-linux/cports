pkgname = "libgusb"
pkgver = "0.4.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "glib-devel",
    "libusb-devel",
    "libgudev-devel",
    "json-glib-devel",
    "vala-devel",
    "usbutils",
]
pkgdesc = "GLib wrapper around libusb"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1b0422bdcd72183272ac42eec9398c5a0bc48a02f618fa3242c468cbbd003049"
# no access to usb in container
options = ["!check", "!cross"]


@subpackage("libgusb-devel")
def _devel(self):
    return self.default_devel()
