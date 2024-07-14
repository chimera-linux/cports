pkgname = "python-lsp-ruff"
pkgver = "2.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-cattrs",
    "python-lsp-server",
    "python-lsprotocol",
    "ruff",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Ruff plugin for python-lsp-server"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/python-lsp/python-lsp-ruff"
source = f"$(PYPI_SITE)/p/python-lsp-ruff/python_lsp_ruff-{pkgver}.tar.gz"
sha256 = "0bb3a227bc136e8ab8c66e91733f2673dc15df6f7fc9eb99d4267d0991b327a5"
# for some reason from inside venv ruff python module can't find the bin
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
