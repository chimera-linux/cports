pkgname = "python-josepy"
pkgver = "2.2.0"
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
sha256 = "74c033151337c854f83efe5305a291686cef723b4b970c43cfe7270cf4a677a9"
