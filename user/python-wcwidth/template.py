pkgname = "python-wcwidth"
pkgver = "0.2.13"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Measure display width of unicode strings in a terminal"
license = "MIT"
url = "https://github.com/jquast/wcwidth"
source = f"$(PYPI_SITE)/w/wcwidth/wcwidth-{pkgver}.tar.gz"
sha256 = "72ea0c06399eb286d978fdedb6923a9eb47e1c486ce63e9b4e64fc18303972b5"


def post_install(self):
    self.install_license("LICENSE")
