pkgname = "python-pytest"
pkgver = "8.4.0"
pkgrel = 0
build_style = "python_pep517"
_deps = [
    "python-iniconfig",
    "python-packaging",
    "python-pluggy",
    "python-pygments",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-sphinx",
    *_deps,
]
depends = [*_deps]
pkgdesc = "Python unit testing framework"
license = "MIT"
url = "https://docs.pytest.org/en/latest"
source = f"$(PYPI_SITE)/p/pytest/pytest-{pkgver}.tar.gz"
sha256 = "14d920b48472ea0dbf68e45b96cd1ffda4705f33307dcc86c676c1b5104838a6"
# missing checkdepends
options = ["!check"]


def post_build(self):
    self.do(
        "make",
        "-C",
        "doc/en",
        "man",
        env={"PYTHONPATH": str(self.chroot_cwd / "build/lib")},
    )


def post_install(self):
    self.install_man("doc/en/_build/man/pytest.1")
    self.install_license("LICENSE")
