pkgname = "python-pytest-rerunfailures"
pkgver = "13.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Pytest plugin to rerun failed tests multiple times"
maintainer = "psykose <alice@ayaya.dev>"
license = "MPL-2.0"
url = "https://github.com/pytest-dev/pytest-rerunfailures"
source = (
    f"$(PYPI_SITE)/p/pytest-rerunfailures/pytest-rerunfailures-{pkgver}.tar.gz"
)
sha256 = "e132dbe420bc476f544b96e7036edd0a69707574209b6677263c950d19b09199"
