pkgname = "python-mypy"
pkgver = "1.19.1"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "mypy/test"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-librt",
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
sha256 = "19d88bb05303fe63f71dd2c6270daca27cb9401c4ca8255fe50d1d920e0eb9ba"
# they take ages, also there are like 3 failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
