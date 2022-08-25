pkgname = "python-requests"
pkgver = "2.28.1"
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
sha256 = "7c5599b102feddaa661c826c56ab4fee28bfd17f5abca1ebbe3e7f19d7c97983"
# needs pytest, is a dependency of pytest
options = ["!check"]
