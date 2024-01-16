pkgname = "python-pytest-timeout"
pkgver = "2.2.0"
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
sha256 = "3b0b95dabf3cb50bac9ef5ca912fa0cfc286526af17afc806824df20c2f72c90"


def post_install(self):
    self.install_license("LICENSE")
