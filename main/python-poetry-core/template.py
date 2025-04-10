pkgname = "python-poetry-core"
pkgver = "2.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-fastjsonschema",
    "python-lark-parser",
    "python-packaging",
]
checkdepends = ["python-pytest"]
pkgdesc = "PEP517 build backend for Poetry"
license = "MIT"
url = "https://github.com/python-poetry/poetry-core"
source = f"$(PYPI_SITE)/p/poetry_core/poetry_core-{pkgver}.tar.gz"
sha256 = "f9dbbbd0ebf9755476a1d57f04b30e9aecf71ca9dc2fcd4b17aba92c0002aa04"
# FIXME
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # prune vendored modules
    self.uninstall(
        "usr/lib/python*/site-packages/poetry/core/_vendor", glob=True
    )
