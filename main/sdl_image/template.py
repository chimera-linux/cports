pkgname = "sdl_image"
pkgver = "2.6.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-jpg-shared",
    "--disable-png-shared",
    "--disable-webp-shared",
    "--disable-tif-shared",
    # defaulting to stb is stupid because the separate libraries are faster
    # and better while being installed on pretty much every system anyway
    "--disable-stb-image",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = [
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libavif-devel",
    "sdl-devel",
]
pkgdesc = "SDL image loading library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_image"
source = f"{url}/release/SDL2_image-{pkgver}.tar.gz"
sha256 = "931c9be5bf1d7c8fae9b7dc157828b7eee874e23c7f24b44ba7eff6b4836312c"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl_image-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
