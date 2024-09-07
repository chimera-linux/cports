pkgname = "python-build"
pkgver = "1.2.2"
pkgrel = 0
hostmakedepends = [
    "python-flit_core",
    "python-installer",
    "python-packaging",
    "python-pyproject_hooks",
]
depends = ["python-pyproject_hooks", "python-packaging"]
pkgdesc = "Simple PEP 517 build frontend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pypa-build.readthedocs.io"
source = f"$(PYPI_SITE)/b/build/build-{pkgver}.tar.gz"
sha256 = "119b2fb462adef986483438377a13b2f42064a2a3a4161f24a0cca698a07ac8c"
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
