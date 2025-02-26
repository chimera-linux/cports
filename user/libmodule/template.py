pkgname = "libmodule"
pkgver = "5.0.1"
pkgrel = 0
build_style = "cmake"
# TODO: cmocka misses .pc which makes it undiscoverable, so skip tests for now
# configure_args = ["-DBUILD_TESTS=true"]
hostmakedepends = [
    "cmake",
    "ninja",
    #    "cmocka",
    "pkgconf",
]
pkgdesc = "Simple and elegant implementation of an actor library in C"
maintainer = "Anthony <w732qq@gmail.com>"
license = "MIT"
url = "https://github.com/FedeDP/libmodule"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "35506360272cb13c0a09f17db6f716cf1c3e9fe40ac1bd574e4dc67916f7ca0a"


@subpackage("libmodule-devel")
def _(self):
    return self.default_devel()
