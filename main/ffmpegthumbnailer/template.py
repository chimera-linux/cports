pkgname = "ffmpegthumbnailer"
pkgver = "2.2.3"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DENABLE_THUMBNAILER=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["ffmpeg-devel", "libjpeg-turbo-devel", "libpng-devel"]
pkgdesc = "Video thumbnailer utilizing ffpmeg"
license = "GPL-2.0-or-later"
url = "https://github.com/dirkvdb/ffmpegthumbnailer"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8c9b9057c6cc8bce9d11701af224c8139c940f734c439a595525e073b09d19b8"


@subpackage("ffmpegthumbnailer-devel")
def _(self):
    return self.default_devel()
