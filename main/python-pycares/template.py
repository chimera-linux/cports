pkgname = "python-pycares"
pkgver = "4.8.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"PYCARES_USE_SYSTEM_LIB": "1"}
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
]
makedepends = ["c-ares-devel", "python-devel"]
depends = ["python-cffi"]
pkgdesc = "Python bindings for c-ares"
license = "MIT"
url = "https://github.com/saghul/pycares"
source = f"$(PYPI_SITE)/p/pycares/pycares-{pkgver}.tar.gz"
sha256 = "2fc2ebfab960f654b3e3cf08a732486950da99393a657f8b44618ad3ed2d39c1"
# tests requires internet access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
