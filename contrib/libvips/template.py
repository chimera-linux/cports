pkgname = "libvips"
pkgver = "8.14.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Db_ndebug=true"]
hostmakedepends = [
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
    "orc-devel",
    "pango-devel",
    "zlib-devel",
]
pkgdesc = "Fast image processing library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libvips/libvips"
source = f"https://github.com/libvips/libvips/releases/download/v{pkgver}/vips-{pkgver}.tar.xz"
sha256 = "90374e9f6fbd5657b5faf306cacda20658d6144d385316b59b865bc1a487b68d"
# FIXME: cfi
hardening = ["vis"]
# broken
options = ["!cross"]


if self.profile().arch == "riscv64":
    broken = "gir generation dies with illegal instruction"


@subpackage("libvips-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libvips-progs")
def _progs(self):
    return self.default_progs()
