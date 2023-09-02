pkgname = "python-build"
pkgver = "1.0.0"
pkgrel = 0
hostmakedepends = [
    "python",
    "python-flit_core",
    "python-packaging",
    "python-pyproject_hooks",
    "python-installer",
]
depends = ["python-pyproject_hooks", "python-packaging"]
pkgdesc = "Simple PEP 517 build frontend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pypa-build.readthedocs.io"
source = f"$(PYPI_SITE)/b/build/build-{pkgver}.tar.gz"
sha256 = "49a60f212df4d9925727c2118e1cbe3abf30b393eff7d0e7287d2170eb36844d"
# no tests
options = ["!check"]


def do_build(self):
    self.do(
        "python",
        "-m",
        "build",
        "--no-isolation",
        "--wheel",
        ".",
        env={"PYTHONPATH": "src"},
    )


def do_install(self):
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
