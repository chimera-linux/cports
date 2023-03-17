pkgname = "python-requests"
pkgver = "2.28.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = [
    "ca-certificates", "python-charset-normalizer",
    "python-urllib3", "python-idna", "python",
]
pkgdesc = "Python HTTP library for human beings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://python-requests.org"
source = f"$(PYPI_SITE)/r/requests/requests-{pkgver}.tar.gz"
sha256 = "98b1b2782e3c6c4904938b84c0eb932721069dfdb9134313beff7c83c2df24bf"
# needs pytest, is a dependency of pytest
options = ["!check"]
