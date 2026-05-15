pkgname = "python-rich"
pkgver = "15.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Python library for rich text and formatting in the terminal"
license = "MIT"
url = "https://rich.readthedocs.io"
source = f"$(PYPI_SITE)/r/rich/rich-{pkgver}.tar.gz"
sha256 = "edd07a4824c6b40189fb7ac9bc4c52536e9780fbbfbddf6f1e2502c31b068c36"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
