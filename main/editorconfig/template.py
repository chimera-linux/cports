pkgname = "editorconfig"
pkgver = "0.12.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pcre2-devel"]
pkgdesc = "EditorConfig core C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://editorconfig.org"
source = f"https://github.com/editorconfig/editorconfig-core-c/archive/v{pkgver}.tar.gz"
sha256 = "36052a5371731d915b53d9c7a24a11c4032585ccacb392ec9d58656eef4c0edf"
# test files not available
options = ["!check"]

@subpackage("editorconfig-devel")
def _devel(self):
    return self.default_devel()
