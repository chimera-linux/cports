pkgname = "python-spake2"
pkgver = "0.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-hkdf"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "SPAKE2 Python implementation"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/warner/python-spake2"
source = f"$(PYPI_SITE)/s/spake2/spake2-{pkgver}.tar.gz"
sha256 = "c17a614b29ee4126206e22181f70a406c618d3c6c62ca6d6779bce95e9c926f4"


def post_install(self):
    self.install_license("LICENSE")
