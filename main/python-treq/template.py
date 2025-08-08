pkgname = "python-treq"
pkgver = "25.5.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs python-httpbin
    "--ignore=src/treq/test/local_httpbin",
    # needs net
    "--deselect=src/treq/test/test_treq_integration.py",
]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-attrs",
    "python-hyperlink",
    "python-incremental",
    "python-requests",
    "python-twisted",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python requests-like API build on top of Twisted"
license = "MIT"
url = "https://github.com/twisted/treq"
source = f"$(PYPI_SITE)/t/treq/treq-{pkgver}.tar.gz"
sha256 = "25dde3a55ae85ec2f2c56332c99aef255ab14f997d0d00552ebff13538a9804a"


def post_install(self):
    self.install_license("LICENSE")
