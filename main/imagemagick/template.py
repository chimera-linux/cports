pkgname = "imagemagick"
pkgver = "7.1.1.47"
pkgrel = 0
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
hostmakedepends = ["pkgconf", "automake", "slibtool", "perl"]
makedepends = [
    "bzip2-devel",
    "djvulibre-devel",
    "djvulibre-devel",
    "fftw-devel",
    "fontconfig-devel",
    "freetype-devel",
    "ghostscript-devel",
    "graphviz-devel",
    "jbigkit-devel",
    "lcms2-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libpng-devel",
    "libpng-devel",
    "libraw-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libtool-devel",
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
license = "ImageMagick"
url = "https://www.imagemagick.org"
source = f"https://github.com/ImageMagick/ImageMagick/archive/{'-'.join(pkgver.rsplit('.', 1))}.tar.gz"
sha256 = "818e21a248986f15a6ba0221ab3ccbaed3d3abee4a6feb4609c6f2432a30d7ed"
# runs out of file descriptors
options = ["!cross", "!check"]

if self.profile().cross:
    hostmakedepends += ["file"]

if self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    makedepends += ["libomp-devel"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("imagemagick-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libmagick")]

    return [
        "usr/lib/libMagick*.so.*",
        "usr/lib/ImageMagick*",
        "usr/share/ImageMagick*",
    ]


@subpackage("imagemagick-perl")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libmagick-perl")]

    return [
        "usr/lib/perl5",
        "usr/share/man/man3/Image::Magick*",
    ]


@subpackage("imagemagick-devel")
def _(self):
    # buildsystem is stupid and does not emit deps
    self.depends += makedepends
    # transitional
    self.provides = [self.with_pkgver("libmagick-devel")]

    return self.default_devel()
