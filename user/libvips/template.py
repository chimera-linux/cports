pkgname = "libvips"
pkgver = "8.17.0"
pkgrel = 1
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
license = "LGPL-2.1-or-later"
url = "https://github.com/libvips/libvips"
source = f"https://github.com/libvips/libvips/releases/download/v{pkgver}/vips-{pkgver}.tar.xz"
sha256 = "8256a82f2e64c119ffadac99822350f45212f16df2505ea8dbae5ff4d0001996"
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
