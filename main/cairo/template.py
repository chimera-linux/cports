pkgname = "cairo"
pkgver = "1.18.0"
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
    "zlib-devel",
    "pixman-devel",
]
checkdepends = ["ghostscript", "libpoppler-devel", "librsvg-devel"]
pkgdesc = "Vector graphics library with cross-device output support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://cairographics.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "243a0736b978a33dee29f9cca7521733b78a65b5418206fef7bd1c3d4cf10b64"
# FIXME int (causes random failures elsewhere)
hardening = ["!int"]
# cyclic, disabled in configure
options = ["!check"]


@subpackage("cairo-devel")
def _devel(self):
    return self.default_devel()
