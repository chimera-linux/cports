pkgname = "python-setuptools-rust"
pkgver = "1.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-semantic_version",
    "python-setuptools",
]
pkgdesc = "Setuptools plugin for Rust support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyO3/setuptools-rust"
source = f"$(PYPI_SITE)/s/setuptools-rust/setuptools-rust-{pkgver}.tar.gz"
sha256 = "c7100999948235a38ae7e555fe199aa66c253dc384b125f5d85473bf81eae3a3"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
