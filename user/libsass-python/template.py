pkgname = "libsass-python"
pkgver = "0.23.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SYSTEM_SASS": "1"}
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
makedepends = ["python-devel", "libsass-devel"]
depends = ["python"]
pkgdesc = "Python bindings for libsass"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "MIT"
url = "https://sass.github.io/libsass-python"
source = (
    f"https://github.com/sass/libsass-python/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "4bff7819756f52f6e4592f03f205104d1ca431088d9452aed5042f89a36f9873"
# Tests require itself to be installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
