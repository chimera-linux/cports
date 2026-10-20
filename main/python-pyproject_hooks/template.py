pkgname = "python-pyproject_hooks"
pkgver = "1.3.3"
pkgrel = 0
hostmakedepends = ["python", "python-flit_core", "python-installer"]
checkdepends = [
    "python-flit_core",
    "python-pip",
    "python-pytest-xdist",
    "python-setuptools",
    "python-testpath",
]
depends = ["python", "python-flit_core"]
pkgdesc = "Low-level library for calling Python build backends"
license = "MIT"
url = "https://pyproject-hooks.readthedocs.io"
source = f"$(PYPI_SITE)/p/pyproject_hooks/pyproject_hooks-{pkgver}.tar.gz"
sha256 = "defda19b854fa0d3bd4f76ea4ddcba8abd7dcfcdd585a6690ade050744fc5f43"
# missing checkdepends
# no licence in tarballs
options = ["!check", "!distlicense"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def check(self):
    self.do("python", "-m", "pytest", "tests", env={"PYTHONPATH": "src"})


def install(self):
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
