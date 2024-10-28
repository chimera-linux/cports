pkgname = "python-treq"
pkgver = "24.9.1"
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
sha256 = "15da7fc404f3e4ed59d0abe5f8eef4966fabbe618039a2a23bc7c15305cefea8"


def post_install(self):
    self.install_license("LICENSE")
