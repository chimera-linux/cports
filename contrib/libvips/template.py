pkgname = "libvips"
pkgver = "8.15.2"
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
    "orc-devel",
    "pango-devel",
    "zlib-devel",
]
pkgdesc = "Fast image processing library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libvips/libvips"
source = f"https://github.com/libvips/libvips/releases/download/v{pkgver}a/vips-{pkgver}.tar.xz"
sha256 = "a2ab15946776ca7721d11cae3215f20f1f097b370ff580cd44fc0f19387aee84"
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
