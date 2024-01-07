pkgname = "python-iniconfig"
pkgver = "2.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
checkdepends = ["python-pytest", "python-py"]
depends = ["python"]
pkgdesc = "Brain-dead simple config-ini parsing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/RonnyPfannschmidt/iniconfig"
source = f"$(PYPI_SITE)/i/iniconfig/iniconfig-{pkgver}.tar.gz"
sha256 = "2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
