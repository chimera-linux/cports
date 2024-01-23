pkgname = "python-openssl"
pkgver = "24.0.0"
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
    "python-flaky",
    "python-pretend",
    "python-pytest",
] + depends
pkgdesc = "Python interface to OpenSSL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://pyopenssl.org"
source = f"$(PYPI_SITE)/p/pyOpenSSL/pyOpenSSL-{pkgver}.tar.gz"
sha256 = "6aa33039a93fffa4563e655b61d11364d01264be8ccb49906101e02a334530bf"
