pkgname = "sdl_image"
pkgver = "2.8.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSDL2IMAGE_AVIF=ON",
    "-DSDL2IMAGE_AVIF_SHARED=ON",
    "-DSDL2IMAGE_JPG=ON",
    "-DSDL2IMAGE_JPG_SHARED=OFF",
    "-DSDL2IMAGE_JXL=ON",
    "-DSDL2IMAGE_JXL_SHARED=ON",
    "-DSDL2IMAGE_PNG=ON",
    "-DSDL2IMAGE_PNG_SHARED=OFF",
    "-DSDL2IMAGE_SAMPLES=OFF",
    "-DSDL2IMAGE_TIF=ON",
    "-DSDL2IMAGE_TIF_SHARED=OFF",
    "-DSDL2IMAGE_WEBP=ON",
    "-DSDL2IMAGE_WEBP_SHARED=OFF",
    # defaulting to stb is stupid because the separate libraries are faster
    # and better while being installed on pretty much every system anyway
    "-DSDL2IMAGE_BACKEND_STB=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libavif-devel",
    "libjxl-devel",
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
    "sdl-devel",
]
pkgdesc = "SDL image loading library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_image"
source = f"{url}/release/SDL2_image-{pkgver}.tar.gz"
sha256 = "4b000f2c238ce380807ee0cb68a0ef005871691ece8646dbf4f425a582b1bb22"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl_image-devel")
def _(self):
    return self.default_devel()
