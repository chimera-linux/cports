pkgname = "imagemagick"
_pver = "7.1.1-11"
pkgver = _pver.replace("-", ".")
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
    "--with-lzma",
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
    "--with-perl-options=INSTALLDIRS=vendor",
    "--with-dejavu-font-dir=/usr/share/fonts/dejavu",
    "--with-gs-font-dir=/usr/share/fonts/Type1",
    # TODO later
    # "--with-jxl",
    # "--with-raqm",
    # "--with-wmf",
    # "--with-openexr",
    # clang 16 implicit decls
    "ac_cv_have_decl_strlcpy=yes",
    "ac_cv_func_strchr=yes",
]
configure_gen = []
make_cmd = "gmake"
# otherwise perl fails
make_install_args = ["MAKE=gmake"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gmake", "perl"]
makedepends = [
    "djvulibre-devel",
    "fftw-devel",
    "libgs-devel",
    "libomp-devel",
    "librsvg-devel",
    "lcms2-devel",
    "libheif-devel",
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "zlib-devel",
    "libbz2-devel",
    "libzstd-devel",
    "graphviz-devel",
    "djvulibre-devel",
    "fontconfig-devel",
    "freetype-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libraw-devel",
    "jbigkit-devel",
    "pango-devel",
    "libxml2-devel",
    "libltdl-devel",
]
checkdepends = ["ghostscript"]
pkgdesc = "Create, edit, compose, or convert digital images"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ImageMagick"
url = "https://www.imagemagick.org"
source = f"https://github.com/ImageMagick/ImageMagick/archive/{_pver}.tar.gz"
sha256 = "98bb2783da7d5b06e7543529bd07b50d034fba611ff15e8817a0f4f73957d934"
# runs out of file descriptors
options = ["!cross", "!check", "keeplibtool"]

if self.profile().cross:
    hostmakedepends += ["file"]


def post_install(self):
    self.install_license("LICENSE")
    # we need to keep the module ones
    for f in (self.destdir / "usr/lib").glob("*.la"):
        f.unlink()


@subpackage("libmagick")
def _lib(self):
    self.pkgdesc = "ImageMagick library"

    return [
        "usr/lib/libMagick*.so.*",
        "usr/lib/ImageMagick*",
        "usr/share/ImageMagick*",
    ]


@subpackage("libmagick-perl")
def _perl(self):
    return [
        "usr/lib/perl5",
        "usr/share/man/man3/Image::Magick*",
    ]


@subpackage("libmagick-devel")
def _devel(self):
    # buildsystem is stupid and does not emit deps
    self.depends += makedepends

    return self.default_devel()
