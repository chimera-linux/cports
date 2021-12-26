pkgname = "cairo"
pkgver = "1.17.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dtee=enabled", "-Dspectre=disabled", "-Dtests=disabled",
    "-Ddefault_library=shared", # do not build static plugins
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "fontconfig-devel", "freetype-bootstrap", "libglib-devel",
    "libpng-devel", "libx11-devel", "libxcb-devel", "libxext-devel",
    "libxrender-devel", "lzo-devel", "zlib-devel", "pixman-devel",
]
pkgdesc = "Vector graphics library with cross-device output support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://cairographics.org"
source = f"{url}/snapshots/{pkgname}-{pkgver}.tar.xz"
sha256 = "74b24c1ed436bbe87499179a3b27c43f4143b8676d8ad237a6fa787401959705"

@subpackage("cairo-devel")
def _devel(self):
    return self.default_devel()
