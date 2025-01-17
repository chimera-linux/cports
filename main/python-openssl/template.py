pkgname = "python-openssl"
pkgver = "25.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-cryptography", "python-typing_extensions"]
checkdepends = [
    "python-pretend",
    "python-pytest",
    "python-pytest-rerunfailures",
    *depends,
]
pkgdesc = "Python interface to OpenSSL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://pyopenssl.org"
source = f"$(PYPI_SITE)/p/pyopenssl/pyopenssl-{pkgver}.tar.gz"
sha256 = "cd2cef799efa3936bb08e8ccb9433a575722b9dd986023f1cabc4ae64e9dac16"
