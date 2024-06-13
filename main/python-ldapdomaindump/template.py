pkgname = "python-ldapdomaindump"
pkgver = "0.9.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-dnspython", "python-ldap3"]
pkgdesc = "Active Directory information dumper via LDAP"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/dirkjanm/ldapdomaindump"
source = f"$(PYPI_SITE)/l/ldapdomaindump/ldapdomaindump-{pkgver}.tar.gz"
sha256 = "99dcda17050a96549966e53bc89e71da670094d53d9542b3b0d0197d035e6f52"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
