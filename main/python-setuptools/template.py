pkgname = "python-setuptools"
pkgver = "59.1.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"
sha256 = "94ee891f4759150cded601a6beb6b08400413aefd0267b692f3f8c6e0bb238e7"
env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1"
}
# missing checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
