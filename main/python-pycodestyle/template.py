pkgname = "python-pycodestyle"
pkgver = "2.11.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python style guide checker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyCQA/pycodestyle"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "757a3dba55dce2ae8b01fe7b46c20cd1e4c0fe794fe6119bce66b942f35e2db0"


def post_install(self):
    self.install_license("LICENSE")
