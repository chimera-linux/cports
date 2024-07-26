pkgname = "onscripter-ru"
pkgver = "3574"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "glew-devel",
    "libass-devel",
    "libepoxy-devel",
    "libpng-devel",
    "libusb-devel",
    "libvorbis-devel",
    "sdl-devel",
    "sdl_image-devel",
    "sdl_mixer-devel",
    "smpeg-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Umineko Project visual novel engine"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later AND BSD-3-Clause"
url = "https://umineko-project.org"
source = f"https://github.com/z-erica/onscripter-ru/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3f7b5349b2634da9da1d123b22b986e01ca4a2cd2f6242df1d689bc239746d9a"


def post_install(self):
    self.install_license("LICENSE-BSD")
