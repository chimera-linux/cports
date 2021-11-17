pkgname = "python-pyyaml"
pkgver = "5.4.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-cython"]
makedepends = ["libyaml-devel", "python-devel"]
pkgdesc = "YAML parser and emitter for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pyyaml.org/wiki/PyYAML"
source = f"$(PYPI_SITE)/P/PyYAML/PyYAML-{pkgver}.tar.gz"
sha256 = "607774cbba28732bfa802b54baa7484215f530991055bb562efbed5b2f20a45e"

def post_install(self):
    self.install_license("LICENSE")
