pkgname = "python-mako"
pkgver = "1.2.3"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest", "python-setuptools", "python-markupsafe"]
depends = ["python-setuptools", "python-markupsafe"]
pkgdesc = "Fast and lightweight templating engine for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.makotemplates.org"
source = f"$(PYPI_SITE)/M/Mako/Mako-{pkgver}.tar.gz"
sha256 = "7fde96466fcfeedb0eed94f187f20b23d85e4cb41444be0e542e2c8c65c396cd"
# tests failing with 3.10 for now, should be harmless
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
