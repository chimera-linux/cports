pkgname = "python-setuptools-rust"
pkgver = "1.10.1"
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
sha256 = "d79035fc54cdf9342e9edf4b009491ecab06c3a652b37c3c137c7ba85547d3e6"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
