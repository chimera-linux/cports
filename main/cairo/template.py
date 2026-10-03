pkgname = "cairo"
pkgver = "1.18.6"
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
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://cairographics.org"
source = f"{url}/releases/cairo-{pkgver}.tar.xz"
sha256 = "1c767308174337a74694da0f3ec069c271452163a1ef4540964c50c301f157d4"
# FIXME int (causes random failures elsewhere)
hardening = ["!int"]
# cyclic, disabled in configure
options = ["!check"]


@subpackage("cairo-devel")
def _(self):
    return self.default_devel()
