pkgname = "python-freezegun"
pkgver = "1.5.1"
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
    *depends,
]
pkgdesc = "Let your python tests travel through time"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/spulec/freezegun"
source = f"$(PYPI_SITE)/f/freezegun/freezegun-{pkgver}.tar.gz"
sha256 = "b29dedfcda6d5e8e083ce71b2b542753ad48cfec44037b3fc79702e2980a89e9"
