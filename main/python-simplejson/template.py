pkgname = "python-simplejson"
pkgver = "3.19.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python JSON encoder and decoder"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT OR AFL-2.1"
url = "https://simplejson.readthedocs.io"
source = f"$(PYPI_SITE)/s/simplejson/simplejson-{pkgver}.tar.gz"
sha256 = "8e086896c36210ab6050f2f9f095a5f1e03c83fa0e7f296d6cba425411364680"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")
