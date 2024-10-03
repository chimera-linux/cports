pkgname = "python-setuptools-rust"
pkgver = "1.10.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
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
sha256 = "5d73e7eee5f87a6417285b617c97088a7c20d1a70fcea60e3bdc94ff567c29dc"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
