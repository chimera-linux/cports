pkgname = "python-treq"
pkgver = "23.11.0"
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
    "python-installer",
    "python-setuptools",
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/twisted/treq"
source = f"$(PYPI_SITE)/t/treq/treq-{pkgver}.tar.gz"
sha256 = "0914ff929fd1632ce16797235260f8bc19d20ff7c459c1deabd65b8c68cbeac5"


def post_install(self):
    self.install_license("LICENSE")
