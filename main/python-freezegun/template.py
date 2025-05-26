pkgname = "python-freezegun"
pkgver = "1.5.2"
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
sha256 = "a54ae1d2f9c02dbf42e02c18a3ab95ab4295818b549a34dac55592d72a905181"
