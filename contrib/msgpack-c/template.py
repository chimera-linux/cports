pkgname = "msgpack-c"
pkgver = "6.0.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
checkdepends = ["gtest-devel"]
pkgdesc = "Binary-based efficient object serialization library (C support)"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "Apache-2.0"
url = "https://msgpack.org"
source = f"https://github.com/msgpack/msgpack-c/archive/c-{pkgver}.tar.gz"
sha256 = "f5b031d7b2f6639936826baeea4d3080e7db5db76838c7230089ec3d1f97e6a2"


@subpackage("msgpack-c-devel")
def _devel(self):
    return self.default_devel()
