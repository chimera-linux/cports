pkgname = "libheif"
pkgver = "1.19.3"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libheif.org"
source = f"https://github.com/strukturag/libheif/archive/v{pkgver}.tar.gz"
sha256 = "3f3b482a5e88b27ba5a10e8bca3309ad9d76ceb9f2f4eef22d390c6ddbd5a2e0"
hardening = ["!vis", "!cfi"]


@subpackage("libheif-devel")
def _(self):
    return self.default_devel()


@subpackage("heif-thumbnailer")
def _(self):
    self.subdesc = "thumbnailer"
    self.install_if = [self.parent]
    return [
        "usr/bin/heif-thumbnailer",
        "usr/share/man/man1/heif-thumbnailer.1",
        "usr/share/thumbnailers",
    ]


@subpackage("libheif-progs")
def _(self):
    return self.default_progs()
