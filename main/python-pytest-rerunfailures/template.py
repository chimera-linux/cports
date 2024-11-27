pkgname = "python-pytest-rerunfailures"
pkgver = "15.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/pytest-dev/pytest-rerunfailures"
source = (
    f"$(PYPI_SITE)/p/pytest-rerunfailures/pytest-rerunfailures-{pkgver}.tar.gz"
)
sha256 = "2d9ac7baf59f4c13ac730b47f6fa80e755d1ba0581da45ce30b72fb3542b4474"
# fail with pytest 8.2
options = ["!check"]
