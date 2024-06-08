pkgname = "rinutils"
pkgver = "0.10.2"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/shlomif/rinutils"
source = f"{url}/releases/download/{pkgver}/rinutils-{pkgver}.tar.xz"
sha256 = "d87fe1199722b7fa9bd508e135383ff0788fbd7d655cbef9757c23212f8c217b"
# needs another 10 perl modules
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
