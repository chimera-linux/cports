pkgname = "python-humanize"
pkgver = "4.12.3"
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
sha256 = "8430be3a615106fdfceb0b2c1b41c4c98c6b0fc5cc59663a5539b111dd325fb0"


def post_install(self):
    self.install_license("LICENCE")
