pkgname = "libgusb"
pkgver = f"0.3.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "libglib-devel", "libusb-devel", "libgudev-devel", "vala-devel", "usbutils"
]
pkgdesc = "GLib wrapper around libusb"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"http://people.freedesktop.org/~hughsient/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "1f51ebe8c91140cffbd1c4d58602c96b884170cae4c74f6f7e302a91d5b7c972"
# no access to usb in container
options = ["!check"]

@subpackage("libgusb-static")
def _static(self):
    return self.default_static()

@subpackage("libgusb-devel")
def _devel(self):
    return self.default_devel()
