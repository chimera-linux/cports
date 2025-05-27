pkgname = "python-pytest-xdist"
pkgver = "3.7.0"
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
sha256 = "42ce53fa3d1aec0e2b6843a082f6fc248412bfc2a27ec454dac2a94967d34e77"


def init_build(self):
    self.env["SETUPTOOLS_SCM_PRETEND_VERSION"] = f"{pkgver}"


def post_install(self):
    self.install_license("LICENSE")
