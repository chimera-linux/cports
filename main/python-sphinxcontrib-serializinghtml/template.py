pkgname = "python-sphinxcontrib-serializinghtml"
pkgver = "1.1.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs serialized HTML document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-serializinghtml/sphinxcontrib_serializinghtml-{pkgver}.tar.gz"
sha256 = "93f3f5dc458b91b192fe10c397e324f262cf163d79f3282c158e8436a2c4511f"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
