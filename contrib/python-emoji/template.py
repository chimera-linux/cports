pkgname = "python-emoji"
pkgver = "2.12.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for emoji support"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/carpedm20/emoji"
source = f"$(PYPI_SITE)/e/emoji/emoji-{pkgver}.tar.gz"
sha256 = "4aa0488817691aa58d83764b6c209f8a27c0b3ab3f89d1b8dceca1a62e4973eb"


def post_install(self):
    self.install_license("LICENSE.txt")
