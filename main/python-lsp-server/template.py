pkgname = "python-lsp-server"
pkgver = "1.13.0"
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
    "python-websockets",
]
checkdepends = [
    "python-flaky",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Python LSP server"
license = "MIT"
url = "https://github.com/python-lsp/python-lsp-server"
source = f"$(PYPI_SITE)/p/python-lsp-server/python_lsp_server-{pkgver}.tar.gz"
sha256 = "378f26b63ecf4c10864de31de5e6da7ad639de9bd60a75d4110fea36fb8d0d69"


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
