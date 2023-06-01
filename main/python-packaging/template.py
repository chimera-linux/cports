pkgname = "python-packaging"
pkgver = "23.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-installer", "python-flit_core"]
checkdepends = ["python-pytest"]
depends = ["python", "python-pyparsing"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR BSD-2-Clause"
url = "https://github.com/pypa/packaging"
source = f"$(PYPI_SITE)/p/packaging/packaging-{pkgver}.tar.gz"
sha256 = "a392980d2b6cffa644431898be54b0045151319d1e7ec34f0cfed48767dd334f"
# needs pytest, is a dependency of pytest
options = ["!check"]


def do_build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
