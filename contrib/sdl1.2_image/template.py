pkgname = "sdl1.2_image"
pkgver = "1.2.12"
pkgrel = 0
build_style = "gnu_configure"
# make sure they're pulled as runtime deps
configure_args = [
    "--disable-jpg-shared",
    "--disable-png-shared",
    "--disable-tif-shared",
    "--disable-webp-shared",
]
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
    "sdl12-compat-devel",
]
pkgdesc = "SDL 1.2 image loading library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://www.libsdl.org/projects/old/SDL_image/release-1.2.html"
source = f"https://www.libsdl.org/projects/SDL_image/release/SDL_image-{pkgver}.tar.gz"
sha256 = "0b90722984561004de84847744d566809dbb9daf732a9e503b91a1b5a84e5699"


@subpackage("sdl1.2_image-devel")
def _(self):
    return self.default_devel()
