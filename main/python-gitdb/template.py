pkgname = "python-gitdb"
pkgver = "4.0.11"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-smmap"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python git object database"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-3-Clause"
url = "https://gitdb.readthedocs.org"
source = f"$(PYPI_SITE)/g/gitdb/gitdb-{pkgver}.tar.gz"
sha256 = "bf5421126136d6d0af55bc1e7c1af1c397a34f5b7bd79e776cd3e89785c2b04b"
# TODO: a bunch of tests want initialised git repo
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
