pkgname = "python-wcwidth"
pkgver = "0.8.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Measure display width of unicode strings in a terminal"
license = "MIT"
url = "https://github.com/jquast/wcwidth"
source = f"$(PYPI_SITE)/w/wcwidth/wcwidth-{pkgver}.tar.gz"
sha256 = "91fbef97204b96a3d4d421609b80340b760cf33e26da123ff243d76b1fda8dda"


def post_install(self):
    self.install_license("LICENSE")
