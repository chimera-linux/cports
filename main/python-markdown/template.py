pkgname = "python-markdown"
pkgver = "3.4.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-flit_core",
    "python-wheel",
]
checkdepends = ["python-pyyaml", "python-pytest"]
depends = ["python"]
pkgdesc = "Python implementation of Markdown"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/Markdown-{pkgver}.tar.gz"
sha256 = "225c6123522495d4119a90b3a3ba31a1e87a70369e03f14799ea9c0d7183a3d6"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
