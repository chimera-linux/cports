pkgname = "msgpack-c"
pkgver = "6.0.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel"]
checkdepends = ["gtest-devel"]
pkgdesc = "Binary-based efficient object serialization library (C support)"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "Apache-2.0"
url = "https://msgpack.org"
source = f"https://github.com/msgpack/msgpack-c/archive/c-{pkgver}.tar.gz"
sha256 = "58d5fe49d0ee2b374d60a61aabf8028b2c92004e6f11bff04e74b639fc8ad541"


@subpackage("msgpack-c-devel")
def _devel(self):
    return self.default_devel()
