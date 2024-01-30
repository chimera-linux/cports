pkgname = "python-dkimpy"
pkgver = "1.1.5"
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
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "BSD-3-Clause"
url = "https://launchpad.net/dkimpy"
source = f"$(PYPI_SITE)/d/dkimpy/dkimpy-{pkgver}.tar.gz"
sha256 = "9a667f8664b72eb9f8aa1250b0757cc3982ab68f70c48af39317b58cf62f2d75"


def post_install(self):
    self.install_license("LICENSE")
