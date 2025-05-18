pkgname = "python-pytest-rerunfailures"
pkgver = "15.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-pytest"]
checkdepends = [*depends]
pkgdesc = "Pytest plugin to rerun failed tests multiple times"
license = "MPL-2.0"
url = "https://github.com/pytest-dev/pytest-rerunfailures"
source = (
    f"$(PYPI_SITE)/p/pytest-rerunfailures/pytest_rerunfailures-{pkgver}.tar.gz"
)
sha256 = "c6040368abd7b8138c5b67288be17d6e5611b7368755ce0465dda0362c8ece80"
# fail with pytest 8.2
options = ["!check"]
