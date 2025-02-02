pkgname = "python-attrs"
pkgver = "25.1.0"
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
sha256 = "1c97078a80c814273a76b2a298a932eb681c87415c11dee0a6921de7f1b02c3e"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
