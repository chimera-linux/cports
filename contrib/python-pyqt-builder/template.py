pkgname = "python-pyqt-builder"
pkgver = "1.15.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
pkgdesc = "PEP517 backend for PyQt projects"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:sip"
url = "https://www.riverbankcomputing.com/software/pyqt-builder"
source = f"$(PYPI_SITE)/P/PyQt-builder/PyQt-builder-{pkgver}.tar.gz"
sha256 = "39f8c75db17d9ce17cb6bbf3df1650b5cebc1ea4e5bd73843d21cc96612b2ae1"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
