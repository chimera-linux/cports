pkgname = "python-cffi"
pkgver = "1.16.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "libffi-devel",
]
makedepends = ["python-devel", "libffi-devel"]
depends = ["python-pycparser"]
checkdepends = ["python-pycparser", "python-pytest"]
pkgdesc = "C FFI for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://cffi.readthedocs.io"
source = f"$(PYPI_SITE)/c/cffi/cffi-{pkgver}.tar.gz"
sha256 = "bcb3ef43e58665bbda2fb198698fcae6776483e0c4a631aa5647806c25e02cc0"
# do_check needs fixing up more
options = ["!check"]


def do_check(self):
    self.do(
        "python",
        "-m",
        "pytest",
        env={
            "PYTHONPATH": str(
                list((self.cwd / "build").glob("lib.*"))[0].relative_to(
                    self.cwd
                )
            )
        },
    )


def post_install(self):
    self.install_license("LICENSE")
