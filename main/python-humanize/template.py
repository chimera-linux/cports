pkgname = "python-humanize"
pkgver = "4.12.1"
pkgrel = 1
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
sha256 = "1338ba97415c96556758a6e2f65977ed406dddf4620d4c6db9bbdfd07f0f1232"


def post_install(self):
    self.install_license("LICENCE")
