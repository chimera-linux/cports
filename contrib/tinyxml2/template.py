pkgname = "tinyxml2"
pkgver = "10.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "C++ XML parser"
maintainer = "xunil-cloud <river_electron@proton.me>"
license = "Zlib"
url = "https://github.com/leethomason/tinyxml2"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3bdf15128ba16686e69bce256cc468e76c7b94ff2c7f391cc5ec09e40bff3839"


@subpackage("tinyxml2-devel")
def _(self):
    return self.default_devel()
