pkgname = "python-smmap"
pkgver = "5.0.1"
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
sha256 = "dceeb6c0028fdb6734471eb07c0cd2aae706ccaecab45965ee83f11c8d3b1f62"


def post_install(self):
    self.install_license("LICENSE")
