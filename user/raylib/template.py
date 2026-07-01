pkgname = "raylib"
pkgver = "6.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_EXTERNAL_GLFW=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_EXAMPLES=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["glfw-devel"]
pkgdesc = "Simple and easy-to-use library to enjoy videogames programming"
license = "Zlib"
url = "https://github.com/raysan5/raylib"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2b3ee1e2120c7a0796b33062c7e9a694dd8a8caa56a96319ac8c8ecf54a90d0b"


@subpackage("raylib-devel")
def _(self):
    return self.default_devel()
