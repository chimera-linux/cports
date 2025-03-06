pkgname = "python-packaging"
pkgver = "24.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = ["python-installer", "python-flit_core"]
checkdepends = ["python-pytest"]
depends = ["python", "python-pyparsing"]
pkgdesc = "Easily build and distribute Python packages"
license = "Apache-2.0 OR BSD-2-Clause"
url = "https://github.com/pypa/packaging"
source = f"$(PYPI_SITE)/p/packaging/packaging-{pkgver}.tar.gz"
sha256 = "c228a6dc5e932d346bc5739379109d49e8853dd8223571c7c5b55260edc0b97f"
# needs pytest, is a dependency of pytest
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
