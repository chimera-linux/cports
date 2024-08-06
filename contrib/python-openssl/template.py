pkgname = "python-openssl"
pkgver = "24.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-cryptography"]
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
sha256 = "4247f0dbe3748d560dcbb2ff3ea01af0f9a1a001ef5f7c4c647956ed8cbf0e95"
