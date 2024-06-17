pkgname = "editorconfig"
pkgver = "0.12.9"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pcre2-devel"]
pkgdesc = "EditorConfig core C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://editorconfig.org"
source = f"https://github.com/editorconfig/editorconfig-core-c/archive/v{pkgver}.tar.gz"
sha256 = "4aaa4e3883332aac7ec19c169dcf128f5f0f963f61d09beb299eb2bce5944e2c"
# test files not available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("editorconfig-devel")
def _devel(self):
    return self.default_devel()
