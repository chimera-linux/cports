pkgname = "libgusb"
pkgver = "0.4.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "glib-devel",
    "json-glib-devel",
    "libgudev-devel",
    "libusb-devel",
    "vala-devel",
]
pkgdesc = "GLib wrapper around libusb"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"{url}/releases/download/{pkgver}/libgusb-{pkgver}.tar.xz"
sha256 = "9df5ef301d6a4b361002aa52cce1165a87a89744055879bdbab31e7e86f1e846"
# no access to usb in container
options = ["!check", "!cross"]


@subpackage("libgusb-devel")
def _(self):
    return self.default_devel()
