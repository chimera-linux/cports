pkgname = "python-requests"
pkgver = "2.27.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = [
    "ca-certificates", "python-charset-normalizer",
    "python-urllib3", "python-idna"
]
pkgdesc = "Python HTTP library for human beings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://python-requests.org"
source = f"$(PYPI_SITE)/r/requests/requests-{pkgver}.tar.gz"
sha256 = "68d7c56fd5a8999887728ef304a6d12edc7be74f1cfa47714fc8b414525c9a61"
# needs pytest, is a dependency of pytest
options = ["!check"]
