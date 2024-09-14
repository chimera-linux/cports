pkgname = "glfw"
pkgver = "3.4"
pkgrel = 2
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
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://www.glfw.org"
source = (
    f"https://github.com/glfw/glfw/releases/download/{pkgver}/glfw-{pkgver}.zip"
)
sha256 = "b5ec004b2712fd08e8861dc271428f048775200a2df719ccf575143ba749a3e9"


@subpackage("glfw-devel")
def _(self):
    self.depends += ["libxrandr-devel", "mesa-devel"]
    return self.default_devel()
