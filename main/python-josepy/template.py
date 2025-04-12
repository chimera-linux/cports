pkgname = "python-josepy"
pkgver = "2.0.0"
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
sha256 = "e7d7acd2fe77435cda76092abe4950bb47b597243a8fb733088615fa6de9ec40"
