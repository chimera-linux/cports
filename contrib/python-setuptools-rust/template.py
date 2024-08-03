pkgname = "python-setuptools-rust"
pkgver = "1.10.0"
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
source = f"$(PYPI_SITE)/s/setuptools-rust/setuptools_rust-{pkgver}.tar.gz"
sha256 = "70a1ca82e2eb9517594585fb4c197e1d39cdee45fe653919fb886c147473cf35"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
