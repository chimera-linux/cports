pkgname = "python-cryptography-vectors"
pkgver = "42.0.7"
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
sha256 = "8294c632dbe2cb14c7b7e24219560e674bc2224dfc4bed577ab077dbb82bfa3c"
# vectors for python-cryptography tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
