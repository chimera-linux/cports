pkgname = "python-pytest-xdist"
pkgver = "3.6.1"
pkgrel = 1
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
checkdepends = ["python-filelock", "python-pexpect", "python-psutil", *depends]
pkgdesc = "Pytest plugin for testing parallelisation"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-xdist"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d8a26b8dbfa97f6f5bee904816b0feb15f3b95eec1e0fcee601535a572a03f5a"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
