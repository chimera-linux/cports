pkgname = "sdl_image"
pkgver = "2.6.2"
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
    "libpng-devel", "libtiff-devel", "libwebp-devel",
    "libavif-devel", "sdl-devel"
]
pkgdesc = "SDL image loading library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_image"
source = f"{url}/release/SDL2_image-{pkgver}.tar.gz"
sha256 = "48355fb4d8d00bac639cd1c4f4a7661c4afef2c212af60b340e06b7059814777"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("sdl_image-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
