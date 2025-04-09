pkgname = "timg"
pkgver = "1.6.1"
pkgrel = 0
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
sha256 = "08147c41ce4cea61b6c494ad746e743b7c4501cfd247bec5134e8ede773bf2af"
