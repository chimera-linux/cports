pkgname = "python-poetry-core"
pkgver = "2.3.1"
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
checkdepends = [
    "git",
    "python-devel",
    "python-pytest-mock",
    "python-tomli-w",
    "python-trove-classifiers",
]
pkgdesc = "PEP517 build backend for Poetry"
license = "MIT"
url = "https://github.com/python-poetry/poetry-core"
source = f"$(PYPI_SITE)/p/poetry_core/poetry_core-{pkgver}.tar.gz"
sha256 = "96f791d5d7d4e040f3983d76779425cf9532690e2756a24fd5ca0f86af19ef82"


def post_install(self):
    self.install_license("LICENSE")
    # prune vendored modules
    self.uninstall(
        "usr/lib/python*/site-packages/poetry/core/_vendor", glob=True
    )
