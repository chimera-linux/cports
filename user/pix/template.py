pkgname = "pix"
pkgver = "3.4.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlibbrasero=false", "-Dwebservices=false"]
hostmakedepends = ["bison", "flex", "gettext", "itstool", "meson", "pkgconf"]
makedepends = [
    "colord-devel",
    "exiv2-devel",
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "lcms2-devel",
    "libheif-devel",
    "libjxl-devel",
    "libpng-devel",
    "libraw-devel",
    "librsvg-devel",
    "libwebp-devel",
    "libx11-devel",
    "xapp-devel",
    "zlib-ng-compat-devel",
]
depends = ["xapp-progs"]
pkgdesc = "Image management application"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/pix/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "38991168a1e90611ca6190ac86c68babc9e93b1705d6274c701af625c26e11aa"


@subpackage("pix-devel")
def _(self):
    return self.default_devel()
