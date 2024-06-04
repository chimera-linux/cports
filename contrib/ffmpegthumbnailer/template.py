pkgname = "ffmpegthumbnailer"
pkgver = "2.2.2"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DENABLE_THUMBNAILER=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["ffmpeg-devel", "libjpeg-turbo-devel", "libpng-devel"]
pkgdesc = "Video thumbnailer utilizing ffpmeg"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/dirkvdb/ffmpegthumbnailer"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8c4c42ab68144a9e2349710d42c0248407a87e7dc0ba4366891905322b331f92"


@subpackage("ffmpegthumbnailer-devel")
def _devel(self):
    return self.default_devel()
