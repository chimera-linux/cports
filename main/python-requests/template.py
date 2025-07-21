pkgname = "python-requests"
pkgver = "2.32.4"
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
    "python",
    "python-charset-normalizer",
    "python-idna",
    "python-urllib3",
]
pkgdesc = "Python HTTP library for human beings"
license = "Apache-2.0"
url = "https://requests.readthedocs.io"
source = f"$(PYPI_SITE)/r/requests/requests-{pkgver}.tar.gz"
sha256 = "27d0316682c8a29834d3264820024b62a36942083d52caf2f14c0591336d3422"
# needs pytest, is a dependency of pytest
options = ["!check"]
