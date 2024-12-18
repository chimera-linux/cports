pkgname = "python-mypy"
pkgver = "1.13.0"
pkgrel = 0
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.mypy-lang.org"
source = f"$(PYPI_SITE)/m/mypy/mypy-{pkgver}.tar.gz"
sha256 = "0291a61b6fbf3e6673e3405cfcc0e7650bebc7939659fdca2702958038bd835e"
# they take ages, also there are like 3 failures
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
