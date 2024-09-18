pkgname = "cairo"
pkgver = "1.18.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dtee=enabled",
    "-Dspectre=disabled",
    "-Dtests=disabled",
    "-Ddefault_library=shared",  # do not build static plugins
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "fontconfig-devel",
    "freetype-bootstrap",
    "glib-bootstrap",
    "libpng-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxext-devel",
    "libxrender-devel",
    "lzo-devel",
    "pixman-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["ghostscript", "poppler-devel", "librsvg-devel"]
pkgdesc = "Vector graphics library with cross-device output support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://cairographics.org"
source = f"{url}/releases/cairo-{pkgver}.tar.xz"
sha256 = "a62b9bb42425e844cc3d6ddde043ff39dbabedd1542eba57a2eb79f85889d45a"
# FIXME int (causes random failures elsewhere)
hardening = ["!int"]
# cyclic, disabled in configure
options = ["!check"]


@subpackage("cairo-devel")
def _(self):
    return self.default_devel()
