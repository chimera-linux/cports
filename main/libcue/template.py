pkgname = "libcue"
pkgver = "2.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "bison", "flex"]
pkgdesc = "CUE sheet parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND BSD-2-Clause"
url = "https://github.com/lipnitsk/libcue"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f27bc3ebb2e892cd9d32a7bee6d84576a60f955f29f748b9b487b173712f1200"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libcue-devel")
def _devel(self):
    return self.default_devel()
