pkgname = "python-fastjsonschema"
pkgver = "2.20.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # hangs
    "--deselect=tests/test_examples.py",
    "--benchmark-skip",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest-benchmark"]
pkgdesc = "Python json schema validator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://horejsek.github.io/python-fastjsonschema"
source = f"$(PYPI_SITE)/f/fastjsonschema/fastjsonschema-{pkgver}.tar.gz"
sha256 = "3d48fc5300ee96f5d116f10fe6f28d938e6008f59a6a025c2649475b87f76a23"


def post_install(self):
    self.install_license("LICENSE")
