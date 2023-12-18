pkgname = "python-flit_core"
pkgver = "3.9.0"
pkgrel = 1
hostmakedepends = ["python"]
checkdepends = ["python-pytest", "python-testpath"]
depends = ["python"]
pkgdesc = "Simplified packaging of Python modules (PEP 517 backend)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://flit.pypa.io"
source = f"$(PYPI_SITE)/f/flit_core/flit_core-{pkgver}.tar.gz"
sha256 = "72ad266176c4a3fcfab5f2930d76896059851240570ce9a98733b658cb786eba"
# missing checkdepends
options = ["!check"]


def do_build(self):
    self.do("python", "-m", "flit_core.wheel")


def do_check(self):
    self.do("python", "-m", "pytest", "flit_core/tests")


def do_install(self):
    from cbuild.util import python

    self.do(
        "python",
        "bootstrap_install.py",
        "--install-root",
        self.chroot_destdir,
        f"dist/flit_core-{pkgver}-py3-none-any.whl",
    )
    python.precompile(self, "usr/lib")
    self.install_license("LICENSE")
