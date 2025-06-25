pkgname = "python-markdown"
pkgver = "3.8.2"
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
sha256 = "247b9a70dd12e27f67431ce62523e675b866d254f900c4fe75ce3dda62237c45"


def check(self):
    self.do("python", "-m", "unittest", "discover")


def post_install(self):
    self.install_license("LICENSE.md")
