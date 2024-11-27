pkgname = "python-filetype"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--benchmark-skip"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest-benchmark"]
depends = ["python"]
pkgdesc = "Python library to infer binary file types"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://h2non.github.io/filetype.py"
source = f"$(PYPI_SITE)/f/filetype/filetype-{pkgver}.tar.gz"
sha256 = "66b56cd6474bf41d8c54660347d37afcc3f7d1970648de365c102ef77548aadb"


def post_install(self):
    self.install_license("LICENSE")
