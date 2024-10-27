pkgname = "python-service-identity"
pkgver = "24.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-hatch_vcs"]
depends = [
    "python-attrs",
    "python-openssl",
    "python-pyasn1",
    "python-pyasn1_modules",
    "python-six",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Service identity verification for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyca/service-identity"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "49fe780f8b15153f23aca32bca763926c1575e1fbabc241eed5634cd21a9202d"


def post_install(self):
    self.install_license("LICENSE")
