pkgname = "python-markdown"
pkgver = "3.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pyyaml"]
depends = ["python"]
pkgdesc = "Python implementation of Markdown"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/markdown-{pkgver}.tar.gz"
sha256 = "7df81e63f0df5c4b24b7d156eb81e4690595239b7d70937d0409f1b0de319c6f"


def check(self):
    self.do("python", "-m", "unittest", "discover")


def post_install(self):
    self.install_license("LICENSE.md")
