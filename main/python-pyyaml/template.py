pkgname = "python-pyyaml"
pkgver = "6.0.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["libyaml-devel", "python-devel"]
depends = ["python"]
pkgdesc = "YAML parser and emitter for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pyyaml.org/wiki/PyYAML"
source = f"$(PYPI_SITE)/P/PyYAML/PyYAML-{pkgver}.tar.gz"
sha256 = "bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43"
# FIXME: fail to run
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
