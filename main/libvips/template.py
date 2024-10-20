pkgname = "libvips"
pkgver = "8.15.5"
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
    "libexif-devel",
    "libexpat-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libpng-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openexr-devel",
    "pango-devel",
    "poppler-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Fast image processing library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libvips/libvips"
source = f"https://github.com/libvips/libvips/releases/download/v{pkgver}/vips-{pkgver}.tar.xz"
sha256 = "2046d2001e60955dc6a85b82afbd6cadc8c34e10ba2f6e5ea09f03fc69eb2603"
# broken
options = ["!cross"]


if self.profile().arch == "riscv64":
    broken = "gir generation dies with illegal instruction"


@subpackage("libvips-devel")
def _(self):
    return self.default_devel()


@subpackage("libvips-progs")
def _(self):
    return self.default_progs()
