pkgname = "python-txtorcon"
pkgver = "24.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = [
    "python-automat",
    "python-cryptography",
    "python-twisted",
    "python-zope.interface",
]
checkdepends = ["lsof", "python-pytest", *depends]
pkgdesc = "Twisted-based Tor controller client"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://txtorcon.readthedocs.io"
source = f"$(PYPI_SITE)/t/txtorcon/txtorcon-{pkgver}.tar.gz"
sha256 = "befe19138d9c8c5307b6ee6d4fe446d0c201ffd1cc404aeb265ed90309978ad0"


def post_install(self):
    self.install_license("LICENSE")
