pkgname = "python-build"
pkgver = "1.6.1"
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
sha256 = "51cc11666391ab6f092070437ac747002ff46f3e4113a3622177ee6b488bfc53"
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
