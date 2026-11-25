pkgname = "libheif"
pkgver = "1.23.7"
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
sha256 = "90e389caad285ca4946461d56d1c115e56bcbb5141d9038050282af91064fbc7"
hardening = ["!vis", "!cfi"]


@split("devel")
def _(self):
    return self.default_devel()


@split("thumbnailer")
def _(self):
    self.subdesc = "thumbnailer"
    self.install_if = [self.parent]
    self.renames = ["heif-thumbnailer"]
    return [
        "cmd:heif-thumbnailer",
        "usr/share/thumbnailers",
    ]


@split("progs")
def _(self):
    return self.default_progs()
