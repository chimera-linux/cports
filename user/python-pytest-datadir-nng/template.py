pkgname = "python-pytest-datadir-nng"
pkgver = "1.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = ["python-pytest"]
pkgdesc = "Fixtures for pytest allowing test functions/methods"
license = "BSD-3-Clause"
url = "https://github.com/jdidion/pytest-datadir-nng"
source = f"$(PYPI_SITE)/p/pytest_datadir_nng/pytest_datadir_nng-{pkgver}.tar.gz"
sha256 = "2a7c3f3322e18d74b8438c4a15a57b5d1cbb95ca534f0041e0ff821b9ac25f89"
# XXX:
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
