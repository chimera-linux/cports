pkgname = "python-pytest"
pkgver = "8.3.5"
pkgrel = 0
build_style = "python_pep517"
_deps = [
    "python-iniconfig",
    "python-packaging",
    "python-pluggy",
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
sha256 = "f4efe70cc14e511565ac476b57c279e12a855b11f48f212af1080ef2263d3845"
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
