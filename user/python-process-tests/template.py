pkgname = "python-process-tests"
pkgver = "3.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Testcase classes and assertions for testing processes"
license = "BSD-2-Clause"
url = "https://pypi.python.org/pypi/process-tests"
source = f"https://github.com/ionelmc/python-process-tests/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a70f444e783a9e5ec987b704711364cb091f960c94523a29981d2c2ae0066bc3"


def post_install(self):
    self.install_license("LICENSE")
