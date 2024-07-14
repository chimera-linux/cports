pkgname = "python-txtorcon"
pkgver = "23.11.0"
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
sha256 = "71f85ae93d76d726510059c9ed74e608bc5a5c9f7d103853b49e414280406a2f"


def post_install(self):
    self.install_license("LICENSE")
