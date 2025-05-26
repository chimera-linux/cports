pkgname = "python-openssl"
pkgver = "25.1.0"
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
license = "Apache-2.0"
url = "https://pyopenssl.org"
source = f"$(PYPI_SITE)/p/pyopenssl/pyopenssl-{pkgver}.tar.gz"
sha256 = "8d031884482e0c67ee92bf9a4d8cceb08d92aba7136432ffb0703c5280fc205b"
