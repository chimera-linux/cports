pkgname = "python-iniconfig"
pkgver = "1.1.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools_scm"]
checkdepends = ["python-pytest", "python-py"]
depends = ["python"]
pkgdesc = "Brain-dead simple config-ini parsing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/RonnyPfannschmidt/iniconfig"
source = f"$(PYPI_SITE)/i/iniconfig/iniconfig-{pkgver}.tar.gz"
sha256 = "bc3af051d7d14b2ee5ef9969666def0cd1a000e121eaea580d4a313df4b37f32"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
