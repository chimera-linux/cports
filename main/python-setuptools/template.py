pkgname = "python-setuptools"
pkgver = "69.0.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"
sha256 = "735896e78a4742605974de002ac60562d286fa8051a7e2299445e8e8fbb01aa6"
env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1",
}
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
