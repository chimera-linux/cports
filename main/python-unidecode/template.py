pkgname = "python-unidecode"
pkgver = "1.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "ASCII transliterations of Unicode text for Python"
license = "GPL-2.0-or-later"
url = "https://pypi.org/project/Unidecode"
source = f"$(PYPI_SITE)/U/Unidecode/Unidecode-{pkgver}.tar.gz"
sha256 = "ce35985008338b676573023acc382d62c264f307c8f7963733405add37ea2b23"


def post_install(self):
    self.install_license("LICENSE")
