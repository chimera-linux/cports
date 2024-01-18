pkgname = "python-service-identity"
pkgver = "24.1.0"
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
checkdepends = ["python-pytest"] + depends
pkgdesc = "Service identity verification for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyca/service-identity"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0a4d5c1e489fe71d379d7c091068a6a6e8e836567bd936006d2ba435a7e14141"


def post_install(self):
    self.install_license("LICENSE")
