pkgname = "python-fastjsonschema"
pkgver = "2.21.1"
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
sha256 = "794d4f0a58f848961ba16af7b9c85a3e88cd360df008c59aac6fc5ae9323b5d4"


def post_install(self):
    self.install_license("LICENSE")
