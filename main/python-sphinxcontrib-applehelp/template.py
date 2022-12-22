pkgname = "python-sphinxcontrib-applehelp"
pkgver = "1.0.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs Apple help book"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-applehelp/sphinxcontrib-applehelp-{pkgver}.tar.gz"
sha256 = "a072735ec80e7675e3f432fcae8610ecf509c5f1869d17e2eecff44389cdbc58"
# circular checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

# FIXME visibility
hardening = ["!vis"]
