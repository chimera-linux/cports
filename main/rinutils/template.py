pkgname = "rinutils"
pkgver = "0.10.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DWITH_TEST_SUITE=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = ["cmocka-devel"]
checkdepends = ["perl-env-path", "perl-path-tiny"]
pkgdesc = "C11 header-only utility library for SchlomiFish projects"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/shlomif/rinutils"
source = f"{url}/releases/download/{pkgver}/rinutils-{pkgver}.tar.xz"
sha256 = "f9e527d37a6cc8c7b8870ada63caa24f32ab0d29fd1116df3ebb686583030955"
# needs another 10 perl modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
