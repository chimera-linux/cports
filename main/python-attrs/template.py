pkgname = "python-attrs"
pkgver = "23.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
checkdepends = ["python-pytest"]  # and other stuff, but does not matter
depends = ["python"]
pkgdesc = "Attributes without boilerplate"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://attrs.readthedocs.io"
source = f"$(PYPI_SITE)/a/attrs/attrs-{pkgver}.tar.gz"
sha256 = "6279836d581513a26f1bf235f9acd333bc9115683f14f7e8fae46c98fc50e015"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
