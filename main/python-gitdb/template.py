pkgname = "python-gitdb"
pkgver = "4.0.12"
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
sha256 = "5ef71f855d191a3326fcfbc0d5da835f26b13fbcba60c32c21091c349ffdb571"
# TODO: a bunch of tests want initialised git repo
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
