pkgname = "libheif"
pkgver = "1.19.7"
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
sha256 = "8334c7c418f82c30c9bec1f46e6abfd5a8d3c420a3210d5505eb1868696ce0cc"
hardening = ["!vis", "!cfi"]


@subpackage("libheif-devel")
def _(self):
    return self.default_devel()


@subpackage("libheif-thumbnailer")
def _(self):
    self.subdesc = "thumbnailer"
    self.install_if = [self.parent]
    # transitional
    self.provides = [self.with_pkgver("heif-thumbnailer")]
    return [
        "usr/bin/heif-thumbnailer",
        "usr/share/man/man1/heif-thumbnailer.1",
        "usr/share/thumbnailers",
    ]


@subpackage("libheif-progs")
def _(self):
    return self.default_progs()
