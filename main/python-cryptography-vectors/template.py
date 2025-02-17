pkgname = "python-cryptography-vectors"
pkgver = "44.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Test vectors for python-cryptography"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = (
    f"$(PYPI_SITE)/c/cryptography_vectors/cryptography_vectors-{pkgver}.tar.gz"
)
sha256 = "5a9866b14465dcfaf12bcdfbc3392987bb559f37ac8b8a4c9b6359be7a3d7ea0"
# vectors for python-cryptography tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
