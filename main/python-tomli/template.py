pkgname = "python-tomli"
pkgver = "2.0.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-flit_core", "python-build", "python-installer"]
depends = ["python"]
pkgdesc = "TOML parser for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/hukkin/tomli"
source = f"$(PYPI_SITE)/t/tomli/tomli-{pkgver}.tar.gz"
sha256 = "de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f"
# no tests in archive
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
