pkgname = "python-freezegun"
pkgver = "1.5.5"
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
sha256 = "ac7742a6cc6c25a2c35e9292dfd554b897b517d2dec26891a2e8debf205cb94a"
