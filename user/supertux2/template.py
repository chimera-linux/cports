pkgname = "supertux2"
pkgver = "0.7.0.1"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DINSTALL_SUBDIR_BIN=bin",
    "-DIS_SUPERTUX_RELEASE=ON",
    "-DUSE_STATIC_SIMPLESQUIRREL=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "curl-devel",
    "fmt-devel",
    "freetype-devel",
    "glew-devel",
    "glm",
    "libogg-devel",
    "libvorbis-devel",
    "openal-soft-devel",
    "physfs-devel",
    "sdl2-compat-devel",
    "sdl2_image-devel",
    "sdl2_net-devel",
    "zlib-ng-devel",
]
pkgdesc = "Classic 2D jump'n run sidescroller game"
license = "GPL-3.0-or-later"
url = "https://supertux.org"
source = f"https://github.com/SuperTux/supertux/releases/download/v{pkgver}/SuperTux-v{pkgver}-Source.tar.gz"
sha256 = "c3a3813bc57b8267960e4fcc33afe5f5cb468abe2a288fe58da4f288d0d7442c"


def post_install(self):
    # contains supertux.png and supertux.xpm, unused by anything
    # since many years ago as the current icon is supertux2
    self.uninstall("usr/share/pixmaps")
