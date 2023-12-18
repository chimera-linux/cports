pkgname = "python-semantic_version"
pkgver = "2.10.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Semantic version comparison for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/rbarrois/python-semanticversion"
source = f"$(PYPI_SITE)/s/semantic-version/semantic_version-{pkgver}.tar.gz"
sha256 = "bdabb6d336998cbb378d4b9db3a4b56a1e3235701dc05ea2690d9a997ed5041c"
# needs django?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
