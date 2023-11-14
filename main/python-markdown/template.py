pkgname = "python-markdown"
pkgver = "3.5.1"
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
sha256 = "b65d7beb248dc22f2e8a31fb706d93798093c308dc1aba295aedeb9d41a813bd"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
