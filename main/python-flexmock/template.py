pkgname = "python-flexmock"
pkgver = "0.12.2"
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
sha256 = "435c661c3b35477575eb9150428a1cfd7c62cb992aa7887567c3357aebc9aca1"


def post_install(self):
    self.install_license("LICENSE")
