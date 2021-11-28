pkgname = "python-alabaster"
pkgver = "0.7.12"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pygments"]
depends = ["python"]
pkgdesc = "Configurable sidebar-enabled Sphinx theme"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://alabaster.readthedocs.io"
source = f"$(PYPI_SITE)/a/alabaster/alabaster-{pkgver}.tar.gz"
sha256 = "a661d72d58e6ea8a57f7a86e37d86716863ee5e92788398526d58b26a4e4dc02"
options = ["lto"]

def post_install(self):
    self.install_license("LICENSE")
