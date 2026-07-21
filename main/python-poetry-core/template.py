pkgname = "python-poetry-core"
pkgver = "2.4.1"
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
sha256 = "89dceb6c10e9c6d8650a16183400e3c9ff9ddee13b0a81023b5575334a2b3744"


def post_install(self):
    self.install_license("LICENSE")
    # prune vendored modules
    self.uninstall(
        "usr/lib/python*/site-packages/poetry/core/_vendor", glob=True
    )
