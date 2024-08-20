pkgname = "double-conversion"
pkgver = "3.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTING=ON", "-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Efficient binary-decimal and decimal-binary routines for doubles"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/google/double-conversion"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "04ec44461850abbf33824da84978043b22554896b552c5fd11a9c5ae4b4d296e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("double-conversion-devel")
def _(self):
    return self.default_devel()
