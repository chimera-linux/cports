pkgname = "python-flake8"
pkgver = "6.0.0"
pkgrel = 0
build_style = "python_module"
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-setuptools"]
depends = ["python-pycodestyle", "python-pyflakes", "python-mccabe"]
checkdepends = ["python-pytest", "python-mock"] + depends
pkgdesc = "Python tool for style guide enforcement"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://flake8.pycqa.org"
source = f"$(PYPI_SITE)/f/flake8/flake8-{pkgver}.tar.gz"
sha256 = "c61007e76655af75e6785a931f452915b371dc48f56efd765247c8fe68f2b181"


def post_install(self):
    self.install_license("LICENSE")
