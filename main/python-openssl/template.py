pkgname = "python-openssl"
pkgver = "26.2.0"
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
sha256 = "8c6fcecd1183a7fc897548dfe388b0cdb7f37e018200d8409cf33959dbe35387"
