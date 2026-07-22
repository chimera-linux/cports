pkgname = "libvips"
pkgver = "8.18.4"
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
    "cgif-devel",
    "fftw-devel",
    "glib-devel",
    "gobject-introspection",
    "highway-devel",
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
pkgdesc = "Fast image processing library"
license = "LGPL-2.1-or-later"
url = "https://github.com/libvips/libvips"
source = f"https://github.com/libvips/libvips/releases/download/v{pkgver}/vips-{pkgver}.tar.xz"
sha256 = "2677bad6c422617fd1172d359c16af34e736965d042c214203a87187d26ff037"
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
