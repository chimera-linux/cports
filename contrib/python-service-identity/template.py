pkgname = "python-service-identity"
pkgver = "21.1.0"
pkgrel = 0
build_style = "python_module"
make_check_target = "tests"
hostmakedepends = ["python-setuptools", "python-wheel"]
depends = [
    "python-attrs",
    "python-openssl",
    "python-pyasn1",
    "python-pyasn1_modules",
    "python-six",
]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Service identity verification for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyca/service-identity"
source = f"$(PYPI_SITE)/s/service-identity/service-identity-{pkgver}.tar.gz"
sha256 = "6e6c6086ca271dc11b033d17c3a8bea9f24ebff920c587da090afc9519419d34"
# fails to find itself
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
