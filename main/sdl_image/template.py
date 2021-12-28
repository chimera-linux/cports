pkgname = "sdl_image"
pkgver = "2.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-jpg-shared",
    "--disable-png-shared",
    "--disable-webp-shared",
    "--disable-tif-shared",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libpng-devel", "libtiff-devel", "libwebp-devel", "sdl-devel"]
pkgdesc = "SDL image loading library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org/projects/SDL_image"
source = f"{url}/release/SDL2_image-{pkgver}.tar.gz"
sha256 = "bdd5f6e026682f7d7e1be0b6051b209da2f402a2dd8bd1c4bd9c25ad263108d0"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("COPYING.txt")

@subpackage("sdl_image-devel")
def _devel(self):
    return self.default_devel()
