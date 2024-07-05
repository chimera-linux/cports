pkgname = "python-dkimpy"
pkgver = "1.1.8"
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
sha256 = "b5f60fb47bbf5d8d762f134bcea0c388eba6b498342a682a21f1686545094b77"


def post_install(self):
    self.install_license("LICENSE")
