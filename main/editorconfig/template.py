pkgname = "editorconfig"
pkgver = "0.12.8"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pcre2-devel"]
pkgdesc = "EditorConfig core C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://editorconfig.org"
source = f"https://github.com/editorconfig/editorconfig-core-c/archive/v{pkgver}.tar.gz"
sha256 = "508f7633416a2ce3c05104ea7daac61c4953803c9935cca6e059086cfa67ee63"
# test files not available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("editorconfig-devel")
def _devel(self):
    return self.default_devel()
