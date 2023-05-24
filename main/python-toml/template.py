pkgname = "python-toml"
pkgver = "0.10.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Python library for TOML"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/uiri/toml"
source = f"$(PYPI_SITE)/t/toml/toml-{pkgver}.tar.gz"
sha256 = "b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"
# needs pytest, is a dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
