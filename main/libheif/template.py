pkgname = "libheif"
pkgver = "1.23.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_DAV1D=ON",
    "-DWITH_GDK_PIXBUF=OFF",
    "-DWITH_JPEG_DECODER=ON",
    "-DWITH_JPEG_ENCODER=ON",
    "-DWITH_UNCOMPRESSED_CODEC=ON",
]
hostmakedepends = ["cmake", "libaom-progs", "ninja", "pkgconf"]
makedepends = [
    "dav1d-devel",
    "libaom-devel",
    "libde265-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "openh264-devel",
    "x264-devel",
    "x265-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "HEIF and AVIF file format decoder and encoder"
license = "LGPL-3.0-or-later"
url = "http://www.libheif.org"
source = f"https://github.com/strukturag/libheif/archive/v{pkgver}.tar.gz"
sha256 = "3be49950c75d3fd9318ba775e8253248dd9e08c61ea955fca81b6b89c02d6b2b"
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
