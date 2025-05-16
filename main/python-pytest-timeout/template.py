pkgname = "python-pytest-timeout"
pkgver = "2.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pexpect", "python-pytest"]
depends = ["python-pytest"]
pkgdesc = "Pytest plugin to abort hanging tests"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-timeout"
source = f"$(PYPI_SITE)/p/pytest-timeout/pytest_timeout-{pkgver}.tar.gz"
sha256 = "7e68e90b01f9eff71332b25001f85c75495fc4e3a836701876183c4bcfd0540a"
# aaaaa
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
