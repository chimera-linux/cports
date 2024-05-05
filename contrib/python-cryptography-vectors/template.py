pkgname = "python-cryptography-vectors"
pkgver = "42.0.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
pkgdesc = "Test vectors for python-cryptography"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = (
    f"$(PYPI_SITE)/c/cryptography_vectors/cryptography_vectors-{pkgver}.tar.gz"
)
sha256 = "47656e3cc5269ba92de8cbf7cfb0891f930a2ea6468154e760d7ca10f6ffd319"
# vectors for python-cryptography tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
