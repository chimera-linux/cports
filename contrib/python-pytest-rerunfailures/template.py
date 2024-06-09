pkgname = "python-pytest-rerunfailures"
pkgver = "14.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Pytest plugin to rerun failed tests multiple times"
maintainer = "psykose <alice@ayaya.dev>"
license = "MPL-2.0"
url = "https://github.com/pytest-dev/pytest-rerunfailures"
source = (
    f"$(PYPI_SITE)/p/pytest-rerunfailures/pytest-rerunfailures-{pkgver}.tar.gz"
)
sha256 = "4a400bcbcd3c7a4ad151ab8afac123d90eca3abe27f98725dc4d9702887d2e92"
# fail with pytest 8.2
options = ["!check"]
