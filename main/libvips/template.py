pkgname = "libvips"
pkgver = "8.18.7"
pkgrel = 0
build_style = "meson"
configure_args = ["-Db_ndebug=true"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "fftw-devel",
    "giflib-devel",
    "glib-devel",
    "gobject-introspection",
    "highway-devel",
    "imagemagick-devel",
    "libarchive-devel",
    "libexif-devel",
    "libexpat-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libpng-devel",
    "libraw-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openexr-devel",
    "pango-devel",
    "poppler-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Image processing library"
license = "LGPL-2.1-or-later"
url = "https://github.com/libvips/libvips"
source = f"https://github.com/libvips/libvips/releases/download/v{pkgver}/vips-{pkgver}.tar.xz"
sha256 = "5baaead3b0bb20ffdb9e9ff09aa9fda08620923df77b63b436654cb5e0b3bf94"
# broken
options = ["!cross"]


@subpackage("libvips-devel")
def _(self):
    return self.default_devel()


@subpackage("libvips-progs")
def _(self):
    return self.default_progs()
