pkgname = "python-pytest-cov"
pkgver = "7.1.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--deselect",
    "tests/test_pytest_cov.py::test_celery",
]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-coverage",
    "python-pluggy",
    "python-pytest",
]
checkdepends = [
    "python-process-tests",
    "python-pytest",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Coverage plugin for pytest"
license = "MIT"
url = "https://pypi.org/project/pytest-cov"
source = f"https://github.com/pytest-dev/pytest-cov/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "17332fbc3674a00ae5a4317b2268b6802e5537674d0ea59f473914cb796d0ef1"


def post_install(self):
    self.install_license("LICENSE")
