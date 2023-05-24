pkgname = "python-flit_core"
pkgver = "3.8.0"
pkgrel = 0
build_wrksrc = "flit_core"
build_style = "python_pep517"
hostmakedepends = ["python-pip"]
checkdepends = ["python-pytest", "python-tomli"]
depends = ["python", "python-tomli"]
pkgdesc = "Simplified packaging of Python modules (PEP 517 backend)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://flit.readthedocs.io"
source = f"$(PYPI_SITE)/f/flit/flit-{pkgver}.tar.gz"
sha256 = "d0f2a8f4bd45dc794befbf5839ecc0fd3830d65a57bd52b5997542fac5d5e937"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("../LICENSE")
