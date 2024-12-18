pkgname = "pix"
pkgver = "3.4.3"
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
sha256 = "ecd6888f7a5272c776338440ddf0ae3199da91421028e0f54c8ca0e422ba0b9a"


@subpackage("pix-devel")
def _(self):
    return self.default_devel()
