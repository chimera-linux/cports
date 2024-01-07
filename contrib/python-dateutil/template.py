pkgname = "python-dateutil"
pkgver = "2.8.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-six"]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Extensions for python datetime"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/dateutil/dateutil"
source = f"$(PYPI_SITE)/p/python-dateutil/python-dateutil-{pkgver}.tar.gz"
sha256 = "0123cacc1627ae19ddf3c27a5de5bd67ee4586fbdd6440d9748f8abb483d3e86"
# pytest-cov
options = ["!check"]
