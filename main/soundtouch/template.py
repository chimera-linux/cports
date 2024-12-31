pkgname = "soundtouch"
pkgver = "2.3.3"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = []
pkgdesc = "SoundTouch audio processing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://www.surina.net/soundtouch"
source = f"{url}/soundtouch-{pkgver}.tar.gz"
sha256 = "43b23dfac2f64a3aff55d64be096ffc7b73842c3f5665caff44975633a975a99"

if self.profile().arch in ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]:
    configure_args += ["-DOPENMP=ON"]
    makedepends += ["libomp-devel"]


@subpackage("soundtouch-devel")
def _(self):
    return self.default_devel()
