pkgname = "python-dkimpy"
pkgver = "1.1.7"
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
sha256 = "393ea47063713482a03cdf512eed5b85e2b657e7f9606e9acfd7b0651d56b04f"


def post_install(self):
    self.install_license("LICENSE")
