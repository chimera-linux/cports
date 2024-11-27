pkgname = "python-lsp-ruff"
pkgver = "2.2.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-lsp/python-lsp-ruff"
source = f"$(PYPI_SITE)/p/python-lsp-ruff/python_lsp_ruff-{pkgver}.tar.gz"
sha256 = "3f80bdb0b4a8ee24624596a1cff60b28cc37771773730f9bf7d946ddff9f0cac"
# for some reason from inside venv ruff python module can't find the bin
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
