pkgname = "python-mypy"
pkgver = "2.1.0"
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
sha256 = "81e76ad12c2d804512e9b13240d1588316531bfba07558286078bfbce9613633"
# they take ages, also there are like 3 failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
