pkgname = "python-requests"
pkgver = "2.31.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
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
url = "https://python-requests.org"
source = f"$(PYPI_SITE)/r/requests/requests-{pkgver}.tar.gz"
sha256 = "942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"
# needs pytest, is a dependency of pytest
options = ["!check"]
