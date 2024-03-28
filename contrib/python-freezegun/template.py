pkgname = "python-freezegun"
pkgver = "1.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-dateutil"]
checkdepends = [
    "python-pytest",
] + depends
pkgdesc = "Let your python tests travel through time"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/spulec/freezegun"
source = f"$(PYPI_SITE)/f/freezegun/freezegun-{pkgver}.tar.gz"
sha256 = "10939b0ba0ff5adaecf3b06a5c2f73071d9678e507c5eaedb23c761d56ac774b"
