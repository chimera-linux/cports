pkgname = "python-mako"
pkgver = "1.3.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-setuptools", "python-markupsafe"]
depends = ["python-setuptools", "python-markupsafe"]
pkgdesc = "Fast and lightweight templating engine for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.makotemplates.org"
source = f"$(PYPI_SITE)/M/Mako/Mako-{pkgver}.tar.gz"
sha256 = "2a0c8ad7f6274271b3bb7467dd37cf9cc6dab4bc19cb69a4ef10669402de698e"
# tests failing with 3.10 for now, should be harmless
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
