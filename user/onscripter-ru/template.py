pkgname = "onscripter-ru"
pkgver = "3572"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "glew-devel",
    "libass-devel",
    "libpng-devel",
    "libusb-devel",
    "libvorbis-devel",
    "sdl-devel",
    "sdl_gpu-devel",
    "sdl_image-devel",
    "sdl_mixer-devel",
    "smpeg-devel",
    "zlib-devel",
]
pkgdesc = "Umineko Project visual novel engine"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later AND BSD-3-Clause"
url = "https://umineko-project.org"
source = f"https://github.com/z-erica/onscripter-ru/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "78a3895ed4518454bfcbaa51c85dae5eb0051fd5653694179039de50ae8430cc"


def post_install(self):
    self.install_license("LICENSE-BSD")
