pkgname = "python-requests"
pkgver = "2.34.2"
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
sha256 = "f288924cae4e29463698d6d60bc6a4da69c89185ad1e0bcc4104f584e960b9ed"
# needs pytest, is a dependency of pytest
options = ["!check"]
