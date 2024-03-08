pkgname = "python-pytest-timeout"
pkgver = "2.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pexpect", "python-pytest"]
depends = ["python-pytest"]
pkgdesc = "Pytest plugin to abort hanging tests"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-timeout"
source = f"$(PYPI_SITE)/p/pytest-timeout/pytest-timeout-{pkgver}.tar.gz"
sha256 = "12397729125c6ecbdaca01035b9e5239d4db97352320af155b3f5de1ba5165d9"


def post_install(self):
    self.install_license("LICENSE")
