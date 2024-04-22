pkgname = "python-pytest-xdist"
pkgver = "3.6.0"
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
sha256 = "f8d2926a28c0ed02fe8e9cc9338060f982c31cb18fd84a21e26602b8a4add849"
# unpackaged filelock
options = ["!check"]


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
