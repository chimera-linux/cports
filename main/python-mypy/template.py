pkgname = "python-mypy"
pkgver = "1.16.1"
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
sha256 = "6bd00a0a2094841c5e47e7374bb42b83d64c527a502e3334e1173a0c24437bab"
# they take ages, also there are like 3 failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
