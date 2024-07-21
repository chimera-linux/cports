pkgname = "python-cryptography-vectors"
pkgver = "43.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Test vectors for python-cryptography"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = (
    f"$(PYPI_SITE)/c/cryptography_vectors/cryptography_vectors-{pkgver}.tar.gz"
)
sha256 = "5c9d09a732d5433cede1542a96ecd70a80e122af047ee7404bcdf1f3ccb8e702"
# vectors for python-cryptography tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
