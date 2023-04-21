pkgname = "python-setuptools"
pkgver = "67.7.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"
sha256 = "bb16732e8eb928922eabaa022f881ae2b7cdcfaf9993ef1f5e841a96d32b8e0c"
env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1"
}
# missing checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
