pkgname = "libcacard"
pkgver = "2.8.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["glib-devel", "nss-devel", "pcsc-lite-devel"]
pkgdesc = "Common Access Card library"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/spice/libcacard"
source = (
    f"https://www.spice-space.org/download/libcacard/libcacard-{pkgver}.tar.xz"
)
sha256 = "fbbf4de8cb7db5bdff5ecb672ff0dbe6939fb9f344b900d51ba6295329a332e7"


@subpackage("libcacard-devel")
def _(self):
    return self.default_devel()
