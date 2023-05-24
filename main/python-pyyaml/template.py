pkgname = "python-pyyaml"
pkgver = "6.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-cython"]
makedepends = ["libyaml-devel", "python-devel"]
depends = ["python"]
pkgdesc = "YAML parser and emitter for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pyyaml.org/wiki/PyYAML"
source = f"$(PYPI_SITE)/P/PyYAML/PyYAML-{pkgver}.tar.gz"
sha256 = "68fb519c14306fec9720a2a5b45bc9f0c8d1b9c72adf45c37baedfcd949c35a2"


def post_install(self):
    self.install_license("LICENSE")
