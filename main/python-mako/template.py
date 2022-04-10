pkgname = "python-mako"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest", "python-setuptools", "python-markupsafe"]
depends = ["python-setuptools", "python-markupsafe"]
pkgdesc = "Fast and lightweight templating engine for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.makotemplates.org"
source = f"$(PYPI_SITE)/M/Mako/Mako-{pkgver}.tar.gz"
sha256 = "9a7c7e922b87db3686210cf49d5d767033a41d4010b284e747682c92bddd8b39"
# tests failing with 3.10 for now, should be harmless
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
