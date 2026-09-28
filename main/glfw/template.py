pkgname = "glfw"
pkgver = "3.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    # manually ran test programs
    "-DGLFW_BUILD_TESTS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "libx11-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "linux-headers",
    "wayland-devel",
]
pkgdesc = "Library for OpenGL window and input"
license = "Zlib"
url = "https://www.glfw.org"
source = (
    f"https://github.com/glfw/glfw/releases/download/{pkgver}/glfw-{pkgver}.zip"
)
sha256 = "ea79bc5feffc254c87291980c2d0bce9acebb68c4983b79f961dcd2cb8a611a0"


@subpackage("glfw-devel")
def _(self):
    self.depends += ["libxrandr-devel", "mesa-devel"]
    return self.default_devel()
