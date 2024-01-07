pkgname = "python-pyproject_hooks"
pkgver = "1.0.0"
pkgrel = 1
hostmakedepends = ["python", "python-flit_core", "python-installer"]
checkdepends = [
    "python-pytest-xdist",
    "python-testpath",
    "python-setuptools",
    "python-flit_core",
    "python-pip",
]
depends = ["python"]
pkgdesc = "Low-level library for calling Python build backends"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pyproject-hooks.readthedocs.io"
source = f"$(PYPI_SITE)/p/pyproject_hooks/pyproject_hooks-{pkgver}.tar.gz"
sha256 = "f271b298b97f5955d53fb12b72c1fb1948c22c1a6b70b315c54cedaca0264ef5"
# missing checkdepends
options = ["!check"]


def do_build(self):
    self.do("python", "-m", "flit_core.wheel")


def do_check(self):
    self.do("python", "-m", "pytest", "tests", env={"PYTHONPATH": "src"})


def do_install(self):
    from cbuild.util import python

    self.do(
        "python",
        "-m",
        "installer",
        "--destdir",
        self.chroot_destdir,
        f"dist/pyproject_hooks-{pkgver}-py3-none-any.whl",
    )
    python.precompile(self, "usr/lib")
    self.install_license("LICENSE")
