pkgname = "sdl3_image"
pkgver = "3.4.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSDLIMAGE_AVIF=ON",
    "-DSDLIMAGE_AVIF_SHARED=ON",
    "-DSDLIMAGE_JPG=ON",
    "-DSDLIMAGE_JPG_SHARED=OFF",
    "-DSDLIMAGE_GIF=ON",
    "-DSDLIMAGE_GIF_SHARED=OFF",
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
provides = [self.with_pkgver("sdl_image")]
pkgdesc = "SDL image loading library"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_image"
source = f"{url}/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "b0c11bbde540e26d1cedf31174349fe6ab67e57658efe22e16e75172859c817d"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl3_image-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_image-devel")]

    return self.default_devel()
