pkgname = "tinyxml2"
pkgver = "10.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "C++ XML parser"
license = "Zlib"
url = "https://github.com/leethomason/tinyxml2"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9da7e1aebbf180ef6f39044b9740a4e96fa69e54a01318488512ae92ca97a685"


@subpackage("tinyxml2-devel")
def _(self):
    return self.default_devel()
