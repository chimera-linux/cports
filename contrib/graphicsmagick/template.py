pkgname = "graphicsmagick"
pkgver = "1.3.42"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--with-modules",
    "--with-perl",
    # FIXME: the jp2 tests fail
    "--without-jp2",
]
hostmakedepends = [
    "automake",
    "libtool",
    "perl",
    "pkgconf",
]
makedepends = [
    "freetype-devel",
    "jasper-devel",
    "jbigkit-devel",
    "lcms2-devel",
    "libde265-devel",
    "libheif-devel",
    "libltdl-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libwebp-devel",
    "libxml2-devel",
]
checkdepends = ["ghostscript"]
pkgdesc = "Swiss army knife of image processing"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "http://www.graphicsmagick.org"
source = f"https://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/{pkgver}/GraphicsMagick-{pkgver}.tar.xz"
sha256 = "484fccfd2b2faf6c2ba9151469ece5072bcb91ba4ed73e75ed3d8e46c759d557"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("Copyright.txt")


@subpackage("graphicsmagick-devel")
def _devel(self):
    return self.default_devel()
