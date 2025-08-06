pkgname = "libheif"
pkgver = "1.20.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_DAV1D=ON",
    "-DWITH_JPEG_DECODER=ON",
    "-DWITH_JPEG_ENCODER=ON",
    "-DWITH_UNCOMPRESSED_CODEC=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "dav1d-devel",
    "gdk-pixbuf-devel",
    "libaom-devel",
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
sha256 = "b70340395d84184bb8dfc833dd51c95ae049435f7ff9abc7b505a08b5ee2bd2a"
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
