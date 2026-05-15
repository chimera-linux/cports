pkgname = "python-markdown"
pkgver = "3.10.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pyyaml"]
depends = ["python"]
pkgdesc = "Python implementation of Markdown"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/markdown-{pkgver}.tar.gz"
sha256 = "994d51325d25ad8aa7ce4ebaec003febcce822c3f8c911e3b17c52f7f589f950"


def check(self):
    self.do("python", "-m", "unittest", "discover")


def post_install(self):
    self.install_license("LICENSE.md")
