pkgname = "python-openssl"
pkgver = "23.2.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-cryptography"]
checkdepends = [
    "python-pytest",
    "python-flaky",
    "python-pretend",
    "python-cryptography",
]
pkgdesc = "Python interface to OpenSSL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://pyopenssl.org"
source = f"$(PYPI_SITE)/p/pyOpenSSL/pyOpenSSL-{pkgver}.tar.gz"
sha256 = "276f931f55a452e7dea69c7173e984eb2a4407ce413c918aa34b55f82f9b8bac"
# unpackaged checkdepends
options = ["!check"]
