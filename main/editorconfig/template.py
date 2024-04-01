pkgname = "editorconfig"
pkgver = "0.12.7"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pcre2-devel"]
pkgdesc = "EditorConfig core C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://editorconfig.org"
source = f"https://github.com/editorconfig/editorconfig-core-c/archive/v{pkgver}.tar.gz"
sha256 = "f89d2e144fd67bdf0d7acfb2ac7618c6f087e1b3f2c3a707656b4180df422195"
# test files not available
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("editorconfig-devel")
def _devel(self):
    return self.default_devel()
