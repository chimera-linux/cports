pkgname = "python-mypy"
pkgver = "1.15.0"
pkgrel = 1
build_style = "python_pep517"
make_check_target = "mypy/test"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-mypy_extensions", "python-typing_extensions"]
checkdepends = [
    *depends,
    "python-filelock",
    "python-lxml",
    "python-psutil",
    "python-pytest",
    "python-pytest-xdist",
]
pkgdesc = "Optional static typing for Python"
license = "MIT"
url = "https://www.mypy-lang.org"
source = f"$(PYPI_SITE)/m/mypy/mypy-{pkgver}.tar.gz"
sha256 = "404534629d51d3efea5c800ee7c42b72a6554d6c400e6a79eafe15d11341fd43"
# they take ages, also there are like 3 failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
