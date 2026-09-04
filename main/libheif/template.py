pkgname = "libheif"
pkgver = "1.23.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_DOCUMENTATION=OFF",
    "-DWITH_DAV1D=ON",
    "-DWITH_GDK_PIXBUF=OFF",
    "-DWITH_JPEG_DECODER=ON",
    "-DWITH_JPEG_ENCODER=ON",
    "-DWITH_OpenH264_DECODER=OFF",
    "-DWITH_UNCOMPRESSED_CODEC=ON",
    "-DWITH_X264=OFF",
    "-DWITH_X264_PLUGIN=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "dav1d-devel",
    "libaom-devel",
    "libaom-devel-static",
    "libaom-progs",
    "libde265-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "x265-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "HEIF and AVIF file format decoder and encoder"
license = "LGPL-3.0-or-later"
url = "http://www.libheif.org"
source = f"https://github.com/strukturag/libheif/archive/v{pkgver}.tar.gz"
sha256 = "0b14d6bdf5680488e3aede354b1e11be1444b3fc4a30fcf2ae06bd6b601466be"
hardening = ["!vis", "!cfi"]


@subpackage("libheif-devel")
def _(self):
    return self.default_devel()


@subpackage("libheif-thumbnailer")
def _(self):
    self.subdesc = "thumbnailer"
    self.install_if = [self.parent]
    self.renames = ["heif-thumbnailer"]
    return [
        "cmd:heif-thumbnailer",
        "usr/share/thumbnailers",
    ]


@subpackage("libheif-progs")
def _(self):
    return self.default_progs()
