pkgname = "python-cryptography-vectors"
pkgver = "45.0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Test vectors for python-cryptography"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = (
    f"$(PYPI_SITE)/c/cryptography_vectors/cryptography_vectors-{pkgver}.tar.gz"
)
sha256 = "fbb0408df8ff2d2b3dbd2928bc5b7feebfdd36fb092fa8790d5778a9b9a1f9ef"
# vectors for python-cryptography tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
