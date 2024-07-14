pkgname = "python-humanize"
pkgver = "4.10.0"
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
sha256 = "06b6eb0293e4b85e8d385397c5868926820db32b9b654b932f57fa41c23c9978"


def post_install(self):
    self.install_license("LICENCE")
