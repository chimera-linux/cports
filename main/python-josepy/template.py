pkgname = "python-josepy"
pkgver = "1.14.0"
pkgrel = 0
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
sha256 = "308b3bf9ce825ad4d4bba76372cf19b5dc1c2ce96a9d298f9642975e64bd13dd"
