pkgname = "python-attrs"
pkgver = "24.3.0"
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
sha256 = "8f5c07333d543103541ba7be0e2ce16eeee8130cb0b3f9238ab904ce1e85baff"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
