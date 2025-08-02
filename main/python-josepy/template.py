pkgname = "python-josepy"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-cryptography"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "JOSE protocol implementation in Python"
license = "Apache-2.0"
url = "https://josepy.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/j/josepy/josepy-{pkgver}.tar.gz"
sha256 = "9beafbaa107ec7128e6c21d86b2bc2aea2f590158e50aca972dca3753046091f"
