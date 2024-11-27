pkgname = "python-lsp-server"
pkgver = "1.12.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = [
    "python-docstring-to-markdown",
    "python-jedi",
    "python-lsp-jsonrpc",
    "python-pluggy",
    "python-ujson",
]
checkdepends = [
    "python-flaky",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Python LSP server"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-lsp/python-lsp-server"
source = f"$(PYPI_SITE)/p/python-lsp-server/python_lsp_server-{pkgver}.tar.gz"
sha256 = "b6a336f128da03bd9bac1e61c3acca6e84242b8b31055a1ccf49d83df9dc053b"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
        # skipping all these deps
        "--ignore=test/plugins",
        "-k",
        "not test_set_flake8_using_workspace_did_change_configuration"
        + " and not test_workspace_loads_pycodestyle_config"
        + " and not test_notebook_document__did_change"
        + " and not test_notebook_document__did_open",
    ]


def post_install(self):
    self.install_license("LICENSE")
