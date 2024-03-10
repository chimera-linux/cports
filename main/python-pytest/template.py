pkgname = "python-pytest"
pkgver = "8.1.1"
pkgrel = 0
build_style = "python_pep517"
_deps = [
    "python-iniconfig",
    "python-packaging",
    "python-pluggy",
    "python-py",
]
hostmakedepends = [
    "gmake",
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-sphinx",
    "python-wheel",
] + _deps
depends = list(_deps)
pkgdesc = "Python unit testing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://docs.pytest.org/en/latest"
source = f"$(PYPI_SITE)/p/pytest/pytest-{pkgver}.tar.gz"
sha256 = "ac978141a75948948817d360297b7aae0fcb9d6ff6bc9ec6d514b85d5a65c044"
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
