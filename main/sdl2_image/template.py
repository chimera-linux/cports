pkgname = "sdl2_image"
pkgver = "2.8.8"
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
    "sdl2-compat-devel",
]
# sigh, dynamically loaded
depends = ["so:libjxl.so.0.11!libjxl", "so:libavif.so.16!libavif"]
provides = [self.with_pkgver("sdl_image")]
pkgdesc = "SDL image loading library"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_image"
source = f"{url}/release/SDL2_image-{pkgver}.tar.gz"
sha256 = "2213b56fdaff2220d0e38c8e420cbe1a83c87374190cba8c70af2156097ce30a"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl2_image-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_image-devel")]

    return self.default_devel()
