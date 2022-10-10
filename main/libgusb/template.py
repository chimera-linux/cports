pkgname = "libgusb"
pkgver = "0.4.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "libglib-devel", "libusb-devel", "libgudev-devel", "json-glib-devel",
    "vala-devel", "usbutils"
]
pkgdesc = "GLib wrapper around libusb"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"http://people.freedesktop.org/~hughsient/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "39ee01dab6a75f28de7c317e25d24159f511e1bf8e7465e275a0fbc483a48b63"
# no access to usb in container
options = ["!check", "!cross"]

@subpackage("libgusb-devel")
def _devel(self):
    return self.default_devel()
