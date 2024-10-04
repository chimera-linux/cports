pkgname = "python-requests"
pkgver = "2.32.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "ca-certificates",
    "python-charset-normalizer",
    "python-urllib3",
    "python-idna",
    "python",
]
pkgdesc = "Python HTTP library for human beings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://requests.readthedocs.io"
source = f"$(PYPI_SITE)/r/requests/requests-{pkgver}.tar.gz"
sha256 = "55365417734eb18255590a9ff9eb97e9e1da868d4ccd6402399eaf68af20a760"
# needs pytest, is a dependency of pytest
options = ["!check"]
