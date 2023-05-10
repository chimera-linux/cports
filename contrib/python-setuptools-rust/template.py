pkgname = "python-setuptools-rust"
pkgver = "1.6.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools_scm"]
depends = [
    "python-semantic_version", "python-setuptools", "python-typing_extensions"
]
pkgdesc = "Setuptools plugin for Rust support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyO3/setuptools-rust"
source = f"$(PYPI_SITE)/s/setuptools-rust/setuptools-rust-{pkgver}.tar.gz"
sha256 = "c86e734deac330597998bfbc08da45187e6b27837e23bd91eadb320732392262"
# unpackaged checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
