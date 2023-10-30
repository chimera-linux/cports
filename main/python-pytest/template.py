pkgname = "python-pytest"
pkgver = "7.4.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "gmake",
    "python-attrs",
    "python-build",
    "python-iniconfig",
    "python-installer",
    "python-pluggy",
    "python-py",
    "python-setuptools_scm",
    "python-sphinx",
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
sha256 = "d989d136982de4e3b29dabcc838ad581c64e8ed52c11fbe86ddebd9da0818cd5"
# missing checkdepends
options = ["!check"]


def post_build(self):
    self.do(
        "gmake",
        "-C",
        "doc/en",
        "man",
        env={"PYTHONPATH": str(self.chroot_cwd / "build/lib")},
    )


def post_install(self):
    self.install_man("doc/en/_build/man/pytest.1")
    self.install_license("LICENSE")
