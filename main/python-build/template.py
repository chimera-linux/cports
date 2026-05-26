pkgname = "python-build"
pkgver = "1.5.0"
pkgrel = 0
hostmakedepends = [
    "python-flit_core",
    "python-installer",
    "python-packaging",
    "python-pyproject_hooks",
]
depends = ["python-pyproject_hooks", "python-packaging"]
pkgdesc = "Simple PEP 517 build frontend"
license = "MIT"
url = "https://pypa-build.readthedocs.io"
source = f"$(PYPI_SITE)/b/build/build-{pkgver}.tar.gz"
sha256 = "302c22c3ba2a0fd5f3911918651341ebb3896176cbdec15bd421f80b1afc7647"
# no tests
options = ["!check"]


def build(self):
    self.do(
        "python",
        "-m",
        "build",
        "--no-isolation",
        "--wheel",
        ".",
        env={"PYTHONPATH": "src"},
    )


def install(self):
    from cbuild.util import python

    self.do(
        "python",
        "-m",
        "installer",
        "--destdir",
        self.chroot_destdir,
        f"dist/build-{pkgver}-py3-none-any.whl",
    )
    python.precompile(self, "usr/lib")
    self.install_license("LICENSE")
