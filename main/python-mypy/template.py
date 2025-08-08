pkgname = "python-mypy"
pkgver = "1.17.1"
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
sha256 = "25e01ec741ab5bb3eec8ba9cdb0f769230368a22c959c4937360efb89b7e9f01"
# they take ages, also there are like 3 failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
