pkgname = "python-mccabe"
pkgver = "0.7.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python McCabe complexity checker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyCQA/mccabe"
source = f"$(PYPI_SITE)/m/mccabe/mccabe-{pkgver}.tar.gz"
sha256 = "348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"


def post_install(self):
    self.install_license("LICENSE")
