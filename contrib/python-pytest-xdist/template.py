pkgname = "python-pytest-xdist"
pkgver = "3.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-execnet",
    "python-pytest",
]
checkdepends = depends
pkgdesc = "Pytest plugin for testing parallelisation"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-xdist"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "803a7dbd7e3ba60cd1f949360155c14d231b8713432ecbe90af6450cb86a9239"
# unpackaged filelock
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def init_check(self):
    self.env["PYTHONPATH"] = "src"


def post_install(self):
    self.install_license("LICENSE")
