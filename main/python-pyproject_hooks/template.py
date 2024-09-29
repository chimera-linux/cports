pkgname = "python-pyproject_hooks"
pkgver = "1.2.0"
pkgrel = 0
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
sha256 = "1e859bd5c40fae9448642dd871adf459e5e2084186e8d2c2a79a824c970da1f8"
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
