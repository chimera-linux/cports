pkgname = "python-attrs"
pkgver = "25.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
checkdepends = ["python-pytest"]  # and other stuff, but does not matter
depends = ["python"]
pkgdesc = "Attributes without boilerplate"
license = "MIT"
url = "https://attrs.readthedocs.io"
source = f"$(PYPI_SITE)/a/attrs/attrs-{pkgver}.tar.gz"
sha256 = "75d7cefc7fb576747b2c81b4442d4d4a1ce0900973527c011d1030fd3bf4af1b"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
