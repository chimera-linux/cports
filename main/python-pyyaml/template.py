pkgname = "python-pyyaml"
pkgver = "6.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
]
makedepends = ["libyaml-devel", "python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "YAML parser and emitter for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pyyaml.org/wiki/PyYAML"
source = f"$(PYPI_SITE)/p/pyyaml/pyyaml-{pkgver}.tar.gz"
sha256 = "d584d9ec91ad65861cc08d42e834324ef890a082e591037abe114850ff7bbc3e"


def post_install(self):
    self.install_license("LICENSE")
