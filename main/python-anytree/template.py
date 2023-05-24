pkgname = "python-anytree"
pkgver = "2.8.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools_scm"]
depends = ["python", "python-six"]
pkgdesc = "Powerful and lightweight Python tree data structure"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/c0fec0de/anytree"
source = f"$(PYPI_SITE)/a/anytree/anytree-{pkgver}.tar.gz"
sha256 = "3f0f93f355a91bc3e6245319bf4c1d50e3416cc7a35cc1133c1ff38306bbccab"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / "usr/LICENSE")
