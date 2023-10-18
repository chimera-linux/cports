pkgname = "python-service-identity"
pkgver = "23.1.0"
pkgrel = 0
build_style = "python_pep517"
make_check_env = {"PYTHONPATH": "src"}
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
depends = [
    "python-attrs",
    "python-openssl",
    "python-pyasn1",
    "python-pyasn1_modules",
    "python-six",
]
checkdepends = ["python-pytest"] + list(depends)
pkgdesc = "Service identity verification for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyca/service-identity"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "35c8caebaa66d1f88e1651a9de32e34fd5323561499f01e918f8e25a19020bd8"
# requires to be installed
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
