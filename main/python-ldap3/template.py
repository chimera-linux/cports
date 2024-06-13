pkgname = "python-ldap3"
pkgver = "2.9.1"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "test"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pyasn1", "python-pycryptodome"]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Strictly RFC 4510-conformant LDAPv3 client for Python"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "LGPL-3.0-or-later"
url = "https://github.com/cannatag/ldap3"
source = f"$(PYPI_SITE)/l/ldap3/ldap3-{pkgver}.tar.gz"
sha256 = "f3e7fc4718e3f09dda568b57100095e0ce58633bcabbed8667ce3f8fbaa4229f"
# TODO: figure out how to get these to work
options = ["!check"]
