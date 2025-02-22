pkgname = "double-conversion"
pkgver = "3.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTING=ON", "-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Efficient binary-decimal and decimal-binary routines for doubles"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/google/double-conversion"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fe54901055c71302dcdc5c3ccbe265a6c191978f3761ce1414d0895d6b0ea90e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("double-conversion-devel")
def _(self):
    return self.default_devel()
