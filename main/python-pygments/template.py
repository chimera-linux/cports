pkgname = "python-pygments"
pkgver = "2.14.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/P/Pygments/Pygments-{pkgver}.tar.gz"
sha256 = "b3ed06a9e8ac9a9aae5a6f5dbe78a8a58655d17b43b93c078f094ddc476ae297"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
