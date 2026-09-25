pkgname = "pix"
pkgver = "3.4.11"
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
depends = ["xapp-progs", "xapp-symbolic-icons"]
pkgdesc = "Image management application"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = f"https://github.com/linuxmint/pix/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "47ac74d19399fdde5d0e2e5d1c2b4a29c3281a549ca7881a1fb8457b1bf5c5eb"


@subpackage("pix-devel")
def _(self):
    return self.default_devel()
