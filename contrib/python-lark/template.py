pkgname = "python-lark"
pkgver = "1.1.9"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--ignore=tests/test_nearley/test_nearley.py"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Parsing toolkit for Python"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/lark-parser/lark"
source = f"$(PYPI_SITE)/l/lark/lark-{pkgver}.tar.gz"
sha256 = "15fa5236490824c2c4aba0e22d2d6d823575dcaf4cdd1848e34b6ad836240fba"


def post_install(self):
    self.install_license("LICENSE")
