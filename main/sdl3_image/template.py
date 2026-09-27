pkgname = "sdl3_image"
pkgver = "3.4.6"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DSDLIMAGE_AVIF=ON",
    "-DSDLIMAGE_AVIF_SHARED=ON",
    "-DSDLIMAGE_JPG=ON",
    "-DSDLIMAGE_JPG_SHARED=OFF",
    "-DSDLIMAGE_GIF=ON",
    "-DSDLIMAGE_JXL=ON",
    "-DSDLIMAGE_JXL_SHARED=ON",
    "-DSDLIMAGE_PNG=ON",
    "-DSDLIMAGE_PNG_SHARED=OFF",
    "-DSDLIMAGE_SAMPLES=OFF",
    "-DSDLIMAGE_TIF=ON",
    "-DSDLIMAGE_TIF_SHARED=OFF",
    "-DSDLIMAGE_WEBP=ON",
    "-DSDLIMAGE_WEBP_SHARED=OFF",
    # defaulting to stb is stupid because the separate libraries are faster
    # and better while being installed on pretty much every system anyway
    "-DSDLIMAGE_BACKEND_STB=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "giflib-devel",
    "libavif-devel",
    "libjxl-devel",
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
    "sdl3-devel",
]
# sigh, dynamically loaded
depends = ["so:libjxl.so.0.11!libjxl", "so:libavif.so.16!libavif"]
pkgdesc = "SDL image loading library"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_image"
source = (
    f"https://libsdl.org/projects/SDL_image/release/SDL3_image-{pkgver}.tar.gz"
)
sha256 = "d2e4637ae700f72e5196b8fbd749850ed2e5e1e09c5a5be8d06ff55aaccf3b01"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl3_image-devel")
def _(self):
    return self.default_devel()
