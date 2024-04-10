pkgname = "python-cryptography-vectors"
pkgver = "42.0.5"
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
sha256 = "505cd5e3b0cb32da1526f07042b7fc38a4b6c356710cb73d2b5f76b037a38ed1"
# vectors for python-cryptography tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
