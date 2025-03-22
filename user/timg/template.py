pkgname = "timg"
pkgver = "1.6.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=MinSizeRel",
    "-DCMAKE_INSTALL_PREFIX=/usr",
    "-DCMAKE_INSTALL_LIBDIR=lib",
    "-DTIMG_VERSION_FROM_GIT=OFF",
    f"-DDISTRIBUTION_VERSION={pkgver}",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "freetype-devel",
    "graphicsmagick-devel",
    "libdeflate-devel",
    "libexif-devel",
    "libjpeg-turbo-devel",
    "librsvg-devel",
    "libsixel-devel",
    "libwebp-devel",
    "poppler-devel",
    "xz-devel",
    "zlib-ng-devel",
]
pkgdesc = "24-Bit color image viewer for terminal"
license = "GPL-2.0-only"
url = "https://github.com/hzeller/timg"
source = f"https://github.com/hzeller/timg/archive/v{pkgver}.tar.gz"
sha256 = "08147c41ce4cea61b6c494ad746e743b7c4501cfd247bec5134e8ede773bf2af"
