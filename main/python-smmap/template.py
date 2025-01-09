pkgname = "python-smmap"
pkgver = "5.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python sliding window memory map manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-3-Clause"
url = "https://smmap.readthedocs.org"
source = f"$(PYPI_SITE)/s/smmap/smmap-{pkgver}.tar.gz"
sha256 = "26ea65a03958fa0c8a1c7e8c7a58fdc77221b8910f6be2131affade476898ad5"


def post_install(self):
    self.install_license("LICENSE")
