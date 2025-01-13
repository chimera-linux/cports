pkgname = "python-poetry-core"
pkgver = "2.0.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-poetry/poetry-core"
source = f"$(PYPI_SITE)/p/poetry_core/poetry_core-{pkgver}.tar.gz"
sha256 = "10177c2772469d9032a49f0d8707af761b1c597cea3b4fb31546e5cd436eb157"
# FIXME
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # prune vendored modules
    self.uninstall(
        "usr/lib/python*/site-packages/poetry/core/_vendor", glob=True
    )
