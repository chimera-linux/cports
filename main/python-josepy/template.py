pkgname = "python-josepy"
pkgver = "1.15.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-cryptography", "python-openssl"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "JOSE protocol implementation in Python"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://josepy.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/j/josepy/josepy-{pkgver}.tar.gz"
sha256 = "46c9b13d1a5104ffbfa5853e555805c915dcde71c2cd91ce5386e84211281223"
