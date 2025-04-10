pkgname = "python-humanize"
pkgver = "4.12.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest", "python-freezegun"]
pkgdesc = "Python humanization utilities"
license = "MIT"
url = "https://humanize.readthedocs.io"
source = f"$(PYPI_SITE)/h/humanize/humanize-{pkgver}.tar.gz"
sha256 = "ce0715740e9caacc982bb89098182cf8ded3552693a433311c6a4ce6f4e12a2c"


def post_install(self):
    self.install_license("LICENCE")
