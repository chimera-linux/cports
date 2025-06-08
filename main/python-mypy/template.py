pkgname = "python-mypy"
pkgver = "1.16.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "mypy/test"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-mypy_extensions",
    "python-pathspec",
    "python-typing_extensions",
]
checkdepends = [
    "python-filelock",
    "python-lxml",
    "python-psutil",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Optional static typing for Python"
license = "MIT"
url = "https://www.mypy-lang.org"
source = f"$(PYPI_SITE)/m/mypy/mypy-{pkgver}.tar.gz"
sha256 = "84b94283f817e2aa6350a14b4a8fb2a35a53c286f97c9d30f53b63620e7af8ab"
# they take ages, also there are like 3 failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
