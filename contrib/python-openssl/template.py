pkgname = "python-openssl"
pkgver = "24.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-cryptography"]
checkdepends = [
    "python-pretend",
    "python-pytest",
    "python-pytest-rerunfailures",
] + depends
pkgdesc = "Python interface to OpenSSL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://pyopenssl.org"
source = f"$(PYPI_SITE)/p/pyOpenSSL/pyOpenSSL-{pkgver}.tar.gz"
sha256 = "cabed4bfaa5df9f1a16c0ef64a0cb65318b5cd077a7eda7d6970131ca2f41a6f"
