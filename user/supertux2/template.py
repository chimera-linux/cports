pkgname = "supertux2"
pkgver = "0.6.3"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DINSTALL_SUBDIR_BIN=bin",
    "-DIS_SUPERTUX_RELEASE=ON",
]
# this is needed because cmake is invoked on submodules in the build stage
make_env = {"CMAKE_POLICY_VERSION_MINIMUM": "3.5"}
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "curl-devel",
    "freetype-devel",
    "glew-devel",
    "glm",
    "libogg-devel",
    "libvorbis-devel",
    "openal-soft-devel",
    "sdl2-compat-devel",
    "sdl2_image-devel",
    "sdl2_net-devel",
    "zlib-ng-devel",
]
pkgdesc = "Classic 2D jump'n run sidescroller game"
license = "GPL-3.0-or-later"
url = "https://supertux.org"
source = f"https://github.com/SuperTux/supertux/releases/download/v{pkgver}/SuperTux-v{pkgver}-Source.tar.gz"
sha256 = "f7940e6009c40226eb34ebab8ffb0e3a894892d891a07b35d0e5762dd41c79f6"
# FIXME lintpixmaps
options = ["!lintpixmaps"]
