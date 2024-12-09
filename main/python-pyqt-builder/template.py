pkgname = "python-pyqt-builder"
pkgver = "1.17.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "custom:sip"
url = "https://github.com/Python-PyQt/PyQt-builder"
source = f"$(PYPI_SITE)/P/PyQt-builder/pyqt_builder-{pkgver}.tar.gz"
sha256 = "fce0e92346d2a4296525b7ad9f02b74ea425f26210390ae0d3e4ca08c31cf4cc"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("pyqtbuild/bundle/qt_wheel_distinfo/LICENSE")
