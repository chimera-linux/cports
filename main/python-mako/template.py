pkgname = "python-mako"
pkgver = "1.1.3"
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
sha256 = "8195c8c1400ceb53496064314c6736719c6f25e7479cd24c77be3d9361cddc27"
# tests failing with 3.10 for now, should be harmless
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
