pkgname = "usbredir"
pkgver = "0.15.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libusb-devel", "glib-devel"]
pkgdesc = "Protocol for redirection USB traffic"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/spice/usbredir"
source = (
    f"https://www.spice-space.org/download/usbredir/usbredir-{pkgver}.tar.xz"
)
sha256 = "6dc2a380277688a068191245dac2ab7063a552999d8ac3ad8e841c10ff050961"


@subpackage("usbredir-devel")
def _(self):
    return self.default_devel()
