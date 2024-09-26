pkgname = "python-spake2"
pkgver = "0.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-cryptography"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "SPAKE2 Python implementation"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/warner/python-spake2"
source = f"$(PYPI_SITE)/s/spake2/spake2-{pkgver}.tar.gz"
sha256 = "421fc4a8d5ac395af7af0206ffd9e6cdf188c105cb1b883d9d683312bb5a9334"


def post_install(self):
    self.install_license("LICENSE")
