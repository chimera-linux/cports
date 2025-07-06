pkgname = "python-pytest-xdist"
pkgver = "3.8.0"
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
checkdepends = ["python-filelock", "python-pexpect", "python-psutil", *depends]
pkgdesc = "Pytest plugin for testing parallelisation"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-xdist"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0badaac301fcd0c4b4ae0e591f70f086b12543087d30bc2b17f0514edba02462"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
