pkgname = "python-flit_core"
pkgver = "3.7.1"
pkgrel = 0
build_wrksrc = f"flit_core"
build_style = "python_pep517"
hostmakedepends = ["python-pip"]
checkdepends = ["python-pytest", "python-tomli"]
depends = ["python-tomli"]
pkgdesc = "Simplified packaging of Python modules (PEP 517 backend)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://flit.readthedocs.io"
source = f"$(PYPI_SITE)/f/flit/flit-{pkgver}.tar.gz"
sha256 = "3c9bd9c140515bfe62dd938c6610d10d6efb9e35cc647fc614fe5fb3a5036682"
# missing checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("../LICENSE")
