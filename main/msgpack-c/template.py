pkgname = "msgpack-c"
pkgver = "6.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
checkdepends = ["gtest-devel"]
pkgdesc = "C library for msgpack"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "Apache-2.0"
url = "https://msgpack.org"
source = f"https://github.com/msgpack/msgpack-c/archive/c-{pkgver}.tar.gz"
sha256 = "c23c4070dbe01f46044bf70c5349f29453d655935b6dc710714c008bca0825a7"


@subpackage("msgpack-c-devel")
def _(self):
    return self.default_devel()
