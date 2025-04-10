pkgname = "python-iniconfig"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
checkdepends = ["python-pytest", "python-py"]
depends = ["python"]
pkgdesc = "Brain-dead simple config-ini parsing"
license = "MIT"
url = "https://github.com/RonnyPfannschmidt/iniconfig"
source = f"$(PYPI_SITE)/i/iniconfig/iniconfig-{pkgver}.tar.gz"
sha256 = "3abbd2e30b36733fee78f9c7f7308f2d0050e88f0087fd25c2645f63c773e1c7"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
