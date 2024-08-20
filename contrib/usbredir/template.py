pkgname = "usbredir"
pkgver = "0.14.0"
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
sha256 = "924dfb5c78328fae45a4c93a01bc83bb72c1310abeed119109255627a8baa332"


@subpackage("usbredir-devel")
def _(self):
    return self.default_devel()
