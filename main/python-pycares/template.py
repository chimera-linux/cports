pkgname = "python-pycares"
pkgver = "4.5.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"PYCARES_USE_SYSTEM_LIB": "1"}
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["c-ares-devel", "python-devel"]
depends = ["python-cffi"]
pkgdesc = "Python bindings for c-ares"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/saghul/pycares"
source = f"$(PYPI_SITE)/p/pycares/pycares-{pkgver}.tar.gz"
sha256 = "025b6c2ffea4e9fb8f9a097381c2fecb24aff23fbd6906e70da22ec9ba60e19d"
# tests requires internet access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
