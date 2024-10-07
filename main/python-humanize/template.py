pkgname = "python-humanize"
pkgver = "4.11.0"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://humanize.readthedocs.io"
source = f"$(PYPI_SITE)/h/humanize/humanize-{pkgver}.tar.gz"
sha256 = "e66f36020a2d5a974c504bd2555cf770621dbdbb6d82f94a6857c0b1ea2608be"


def post_install(self):
    self.install_license("LICENCE")
