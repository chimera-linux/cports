pkgname = "tinyxml2"
pkgver = "11.0.0"
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
sha256 = "5556deb5081fb246ee92afae73efd943c889cef0cafea92b0b82422d6a18f289"


@subpackage("tinyxml2-devel")
def _(self):
    return self.default_devel()
