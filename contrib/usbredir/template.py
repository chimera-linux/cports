pkgname = "usbredir"
pkgver = "0.13.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libusb-devel", "glib-devel"]
pkgdesc = "Protocol for redirection USB traffic"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/spice/usbredir"
source = (
    f"https://www.spice-space.org/download/usbredir/usbredir-{pkgver}.tar.xz"
)
sha256 = "4ba6faa02c0ae6deeb4c53883d66ab54b3a5899bead42ce4ded9568b9a7dc46e"


@subpackage("usbredir-devel")
def _devel(self):
    return self.default_devel()
