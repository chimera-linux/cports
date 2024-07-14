pkgname = "ruff-lsp"
pkgver = "0.0.54"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-lsprotocol",
    "python-packaging",
    "python-pygls",
    "ruff",
]
checkdepends = [
    "python-lsp-jsonrpc",
    "python-pytest-asyncio",
    *depends,
]
pkgdesc = "LSP server for ruff"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/astral-sh/ruff-lsp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fa5809a234e96c81da275100556929c64ae38abb18bddb12add8a0c0a24694b4"


def post_install(self):
    self.install_license("LICENSE")
