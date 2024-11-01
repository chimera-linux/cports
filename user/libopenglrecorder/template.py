pkgname = "libopenglrecorder"
pkgver = "0.1.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libjpeg-turbo-devel",
    "libpulse-devel",
    "libvorbis-devel",
    "libvpx-devel",
    "openh264-devel",
]
pkgdesc = "OpenGL recording library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Benau/libopenglrecorder"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a90a99c23f868636f77003a8dc6ffe6c3699fc2759c47df5dbd44ff8b42d2e4f"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libopenglrecorder-devel")
def _(self):
    return self.default_devel()
