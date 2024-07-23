pkgname = "libheif"
pkgver = "1.18.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_DAV1D=ON",
    "-DWITH_JPEG_DECODER=ON",
    "-DWITH_JPEG_ENCODER=ON",
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
]
pkgdesc = "HEIF and AVIF file format decoder and encoder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libheif.org"
source = f"https://github.com/strukturag/libheif/archive/v{pkgver}.tar.gz"
sha256 = "73bc94442038d44d56fe730f72516ae53134eb15b878a7ad89ef60fac93a3318"
hardening = ["!vis", "!cfi"]
# needs full symbol visibility
options = ["!check"]


@subpackage("libheif-devel")
def _devel(self):
    return self.default_devel()


@subpackage("heif-thumbnailer")
def _thumbnailer(self):
    self.subdesc = "thumbnailer"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/bin/heif-thumbnailer",
        "usr/share/man/man1/heif-thumbnailer.1",
        "usr/share/thumbnailers",
    ]


@subpackage("libheif-progs")
def _progs(self):
    return self.default_progs()
