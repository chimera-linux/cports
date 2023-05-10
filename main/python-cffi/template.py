pkgname = "python-cffi"
pkgver = "1.15.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "libffi-devel"]
makedepends = ["python-devel", "libffi-devel"]
depends = ["python-pycparser"]
checkdepends = ["python-pycparser", "python-pytest"]
pkgdesc = "C FFI for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://cffi.readthedocs.io"
source = f"$(PYPI_SITE)/c/cffi/cffi-{pkgver}.tar.gz"
sha256 = "d400bfb9a37b1351253cb402671cea7e89bdecc294e8016a707f6d1d8ac934f9"
# do_check needs fixing up more
options = ["!check"]

def do_check(self):
    self.do("python", "-m", "pytest", env = {
        "PYTHONPATH": str(
            list((self.cwd / "build").glob("lib.*"))[0].relative_to(self.cwd)
        )
    })

def post_install(self):
    self.install_license("LICENSE")
