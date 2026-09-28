pkgname = "timg"
pkgver = "1.6.3"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DTIMG_VERSION_FROM_GIT=OFF",
    f"-DDISTRIBUTION_VERSION={pkgver}",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "graphicsmagick-devel",
    "libdeflate-devel",
    "libexif-devel",
    "libjpeg-turbo-devel",
    "librsvg-devel",
    "libsixel-devel",
    "poppler-devel",
]
pkgdesc = "Terminal image viewer"
license = "GPL-2.0-only"
url = "https://github.com/hzeller/timg"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "59c908867f18c81106385a43065c232e63236e120d5b2596b179ce56340d7b01"
