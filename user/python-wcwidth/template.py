pkgname = "python-wcwidth"
pkgver = "0.2.14"
pkgrel = 0
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
sha256 = "4d478375d31bc5395a3c55c40ccdf3354688364cd61c4f6adacaa9215d0b3605"


def post_install(self):
    self.install_license("LICENSE")
