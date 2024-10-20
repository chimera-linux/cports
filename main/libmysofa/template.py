pkgname = "libmysofa"
pkgver = "1.3.3"
pkgrel = 0
build_style = "cmake"
# tests fail when run in parallel
make_check_args = ["-j1"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["cunit-devel", "zlib-ng-compat-devel"]
checkdepends = ["nodejs"]
pkgdesc = "Reader for AES SOFA files to get better HRTFs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/hoene/libmysofa"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a15f7236a2b492f8d8da69f6c71b5bde1ef1bac0ef428b94dfca1cabcb24c84f"
# FIXME: breaks fail-issue-167a test
hardening = ["!int"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libmysofa-devel")
def _(self):
    return self.default_devel()
