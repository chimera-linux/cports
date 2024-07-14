pkgname = "python-lsp-server"
pkgver = "1.11.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/python-lsp/python-lsp-server"
source = f"$(PYPI_SITE)/p/python-lsp-server/python-lsp-server-{pkgver}.tar.gz"
sha256 = "89edd6fb3f7852e4bf5a3d1d95ea41484d1a28fa94b6e3cbff12b9db123b8e86"


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
