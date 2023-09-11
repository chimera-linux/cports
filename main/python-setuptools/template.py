pkgname = "python-setuptools"
pkgver = "68.2.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"
sha256 = "56ee14884fd8d0cd015411f4a13f40b4356775a0aefd9ebc1d3bfb9a1acb32f1"
env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1",
}
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
