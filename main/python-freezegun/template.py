pkgname = "python-freezegun"
pkgver = "1.5.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-dateutil"]
checkdepends = [
    "python-pytest",
    *depends,
]
pkgdesc = "Let your python tests travel through time"
license = "Apache-2.0"
url = "https://github.com/spulec/freezegun"
source = f"$(PYPI_SITE)/f/freezegun/freezegun-{pkgver}.tar.gz"
sha256 = "798b9372fdd4d907f33e8b6a58bc64e682d9ffa8d494ce60f780197ee81faed1"
