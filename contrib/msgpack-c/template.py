# nb: C and C++ support are distincts since v4.x
pkgname = "msgpack-c"
pkgver = "6.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel"]
checkdepends = ["gtest-devel"]
pkgdesc = "Binary-based efficient object serialization library (C support)"
license = "Apache-2.0"
url = "https://msgpack.org"
source = f"https://github.com/msgpack/msgpack-c/archive/c-{pkgver}.tar.gz"
sha256 = "af6f3cf25edb220aa2140b09bb5bdd73ddf00938194bd94ebe5c92090cccb466"

@subpackage("msgpack-c-devel")
def _devel(self):
    return self.default_devel()
