pkgname = "python-flexmock"
pkgver = "0.12.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Testing library that makes it easy to create mocks, stubs and fakes"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/flexmock/flexmock"
source = f"$(PYPI_SITE)/f/flexmock/flexmock-{pkgver}.tar.gz"
sha256 = "20b690afa4ff8c6f31548d896d6d41cca1fc9050a4cf628b965ea434ec548ee3"


def post_install(self):
    self.install_license("LICENSE")
