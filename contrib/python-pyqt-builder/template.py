pkgname = "python-pyqt-builder"
pkgver = "1.16.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "PEP517 backend for PyQt projects"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:sip"
url = "https://github.com/Python-PyQt/PyQt-builder"
source = f"$(PYPI_SITE)/P/PyQt-builder/pyqt_builder-{pkgver}.tar.gz"
sha256 = "3ce5c03dc3fc856b782da3f53b4f3f3b6556aad7bd8416d7bbfc274d03bcf032"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("pyqtbuild/bundle/qt_wheel_distinfo/LICENSE")
