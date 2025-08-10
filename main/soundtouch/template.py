pkgname = "soundtouch"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = []
pkgdesc = "SoundTouch audio processing library"
license = "LGPL-2.1-only"
url = "https://www.surina.net/soundtouch"
source = f"{url}/soundtouch-{pkgver}.tar.gz"
sha256 = "3dda3c9ab1e287f15028c010a66ab7145fa855dfa62763538f341e70b4d10abd"

if self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    configure_args += ["-DOPENMP=ON"]
    makedepends += ["libomp-devel"]


@subpackage("soundtouch-devel")
def _(self):
    return self.default_devel()
