pkgname = "python-poetry-core"
pkgver = "1.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
]
depends = ["python-fastjsonschema", "python-lark"]
checkdepends = [
    "git",
    "python-devel",
    "python-pytest",
    "python-pytest-mock",
    "python-setuptools",
    "python-tomli-w",
    "python-virtualenv",
] + depends
pkgdesc = "PEP 517 build backend implementation developed for Poetry"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/python-poetry/poetry-core"
source = f"$(PYPI_SITE)/p/poetry-core/poetry_core-{pkgver}.tar.gz"
sha256 = "fa7a4001eae8aa572ee84f35feb510b321bd652e5cf9293249d62853e1f935a2"


def post_install(self):
    self.install_license("LICENSE")
