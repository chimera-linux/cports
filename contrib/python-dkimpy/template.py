pkgname = "python-dkimpy"
pkgver = "1.1.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-aiodns",
    "python-authres",
    "python-dnspython",
    "python-pynacl",
]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Python library that implements DKIM email signing and verification"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://launchpad.net/dkimpy"
source = f"$(PYPI_SITE)/d/dkimpy/dkimpy-{pkgver}.tar.gz"
sha256 = "0ce72d961f443e8f9f05694b354542dee534e08e2b8c5b60c62d5daca7c1da0f"


def post_install(self):
    self.install_license("LICENSE")
