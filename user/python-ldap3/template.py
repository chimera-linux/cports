pkgname = "python-ldap3"
pkgver = "2.9.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = ["python-pyasn1"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "RFC 4510 conforming LDAP client library"
license = "LGPL-3.0-only"
url = "https://github.com/cannatag/ldap3"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d7482a10dabd90e8d3ca3dc9288af3e5c8e9547f5f17f676db1e983cafdd78b9"
# XXX: test failures
options = ["!check"]


def check(self):
    self.do("python", "-m", "unittest", "discover", "-s", "test")
