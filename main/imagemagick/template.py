pkgname = "imagemagick"
pkgver = "7.1.1.41"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-opencl",
    "--with-modules",
    "--with-bzlib",
    "--with-djvu",
    "--with-fftw",
    "--with-fontconfig",
    "--with-freetype",
    "--with-gslib",
    "--with-gvc",
    "--with-heic",
    "--with-jbig",
    "--with-jpeg",
    "--with-jxl",
    "--with-lzma",
    "--with-openexr",
    "--with-openjp2",
    "--with-pango",
    "--with-perl",
    "--with-png",
    "--with-raw",
    "--with-rsvg",
    "--with-tiff",
    "--with-webp",
    "--with-xml",
    "--with-zlib",
    "--with-zstd",
    "--with-perl-options=INSTALLDIRS=vendor INSTALL_BASE=",
    "--with-dejavu-font-dir=/usr/share/fonts/dejavu",
    "--with-gs-font-dir=/usr/share/fonts/Type1",
    # TODO later
    # "--with-raqm",
    # "--with-wmf",
]
configure_gen = []
hostmakedepends = ["pkgconf", "automake", "libtool", "perl"]
makedepends = [
    "bzip2-devel",
    "djvulibre-devel",
    "djvulibre-devel",
    "fftw-devel",
    "fontconfig-devel",
    "freetype-devel",
    "graphviz-devel",
    "jbigkit-devel",
    "lcms2-devel",
    "libgs-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libltdl-devel",
    "libomp-devel",
    "libpng-devel",
    "libpng-devel",
    "libraw-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxml2-devel",
    "openexr-devel",
    "openjpeg-devel",
    "pango-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = ["ghostscript"]
pkgdesc = "Create, edit, compose, or convert digital images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ImageMagick"
url = "https://www.imagemagick.org"
source = f"https://github.com/ImageMagick/ImageMagick/archive/{'-'.join(pkgver.rsplit('.', 1))}.tar.gz"
sha256 = "cabf2516dce66da56dd4e3071453b808eefaf4326a93292d2a222a4ea623d601"
# runs out of file descriptors
options = ["!cross", "!check"]

if self.profile().cross:
    hostmakedepends += ["file"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libmagick")
def _(self):
    self.pkgdesc = "ImageMagick library"

    return [
        "usr/lib/libMagick*.so.*",
        "usr/lib/ImageMagick*",
        "usr/share/ImageMagick*",
    ]


@subpackage("libmagick-perl")
def _(self):
    return [
        "usr/lib/perl5",
        "usr/share/man/man3/Image::Magick*",
    ]


@subpackage("libmagick-devel")
def _(self):
    # buildsystem is stupid and does not emit deps
    self.depends += makedepends

    return self.default_devel()
