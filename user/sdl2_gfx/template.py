pkgname = "sdl2_gfx"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-mmx"]
hostmakedepends = ["automake", "slibtool", "pkgconf"]
makedepends = ["sdl2-compat-devel"]
pkgdesc = "SDL2 graphics drawing primitives and other support functions"
maintainer = "peri <peri@periwinkle.sh>"
license = "Zlib"
url = "https://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx"
source = f"http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-{pkgver}.tar.gz"
sha256 = "63e0e01addedc9df2f85b93a248f06e8a04affa014a835c2ea34bfe34e576262"


def post_install(self):
    self.install_license("COPYING")


@subpackage("sdl2_gfx-devel")
def _(self):
    return self.default_devel()
