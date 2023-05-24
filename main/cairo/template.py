pkgname = "cairo"
pkgver = "1.17.8"
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
    "glib-devel",
    "libpng-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxext-devel",
    "libxrender-devel",
    "lzo-devel",
    "zlib-devel",
    "pixman-devel",
]
checkdepends = ["ghostscript", "libpoppler-glib-devel", "librsvg-devel"]
pkgdesc = "Vector graphics library with cross-device output support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://cairographics.org"
source = f"{url}/snapshots/{pkgname}-{pkgver}.tar.xz"
sha256 = "5b10c8892d1b58d70d3f0ba5b47863a061262fa56b9dc7944161f8c8b783bc64"
# FIXME int (causes random failures elsewhere)
hardening = ["!int"]
# cyclic, disabled in configure
options = ["!check"]


@subpackage("cairo-devel")
def _devel(self):
    return self.default_devel()
