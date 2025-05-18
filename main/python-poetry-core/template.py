pkgname = "python-poetry-core"
pkgver = "2.1.3"
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
sha256 = "0522a015477ed622c89aad56a477a57813cace0c8e7ff2a2906b7ef4a2e296a4"


def post_install(self):
    self.install_license("LICENSE")
    # prune vendored modules
    self.uninstall(
        "usr/lib/python*/site-packages/poetry/core/_vendor", glob=True
    )
