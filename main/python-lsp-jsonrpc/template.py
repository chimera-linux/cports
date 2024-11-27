pkgname = "python-lsp-jsonrpc"
pkgver = "1.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python-ujson"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python implementation of the JSON RPC 2.0 protocol"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-lsp/python-lsp-jsonrpc"
source = f"$(PYPI_SITE)/p/python-lsp-jsonrpc/python-lsp-jsonrpc-{pkgver}.tar.gz"
sha256 = "4688e453eef55cd952bff762c705cedefa12055c0aec17a06f595bcc002cc912"


def post_install(self):
    self.install_license("LICENSE")
