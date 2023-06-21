pkgname = "python-pytest"
pkgver = "7.3.2"
pkgrel = 0
build_style = "python_module"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "python-setuptools_scm",
    "python-sphinx",
    "python-attrs",
    "python-iniconfig",
    "python-py",
    "python-pluggy",
    "python-wheel",
]
depends = [
    "python-packaging",
    "python-tomli",
    "python-attrs",
    "python-iniconfig",
    "python-py",
    "python-pluggy",
    "python",
]
pkgdesc = "Python unit testing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://docs.pytest.org/en/latest"
source = f"$(PYPI_SITE)/p/pytest/pytest-{pkgver}.tar.gz"
sha256 = "ee990a3cc55ba808b80795a79944756f315c67c12b56abd3ac993a7b8c17030b"
# missing checkdepends
options = ["!check"]


def post_build(self):
    from cbuild.util import make

    make.Make(self).invoke(
        None,
        ["-C", "doc/en", "man"],
        env={"PYTHONPATH": str(self.chroot_cwd / "build/lib")},
    )


def post_install(self):
    self.install_man("doc/en/_build/man/pytest.1")
    self.install_license("LICENSE")
