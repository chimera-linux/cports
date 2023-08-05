pkgname = "python-pyflakes"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python code linter"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyCQA/pyflakes"
source = f"$(PYPI_SITE)/p/pyflakes/pyflakes-{pkgver}.tar.gz"
sha256 = "a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"


def post_install(self):
    self.install_license("LICENSE")
