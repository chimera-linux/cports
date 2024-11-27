pkgname = "python-dateutil"
pkgver = "2.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-six"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Extensions for python datetime"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/dateutil/dateutil"
source = f"$(PYPI_SITE)/p/python-dateutil/python-dateutil-{pkgver}.tar.gz"
sha256 = "78e73e19c63f5b20ffa567001531680d939dc042bf7850431877645523c66709"
# cycle with python-freezegun
options = ["!check"]
