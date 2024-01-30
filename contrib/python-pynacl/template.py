pkgname = "python-pynacl"
pkgver = "1.5.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SODIUM_INSTALL": "system"}
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["libsodium-devel", "python-devel"]
checkdepends = ["python-hypothesis", "python-pytest"]
depends = ["python-cffi"]
pkgdesc = "Python bindings for libsodium"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "Apache-2.0"
url = "https://github.com/pyca/pynacl"
source = f"$(PYPI_SITE)/P/PyNaCl/PyNaCl-{pkgver}.tar.gz"
sha256 = "8ac7448f09ab85811607bdd21ec2464495ac8b7c66d146bf545b0f08fb9220ba"


def post_install(self):
    self.install_license("LICENSE")
