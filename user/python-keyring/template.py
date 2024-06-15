pkgname = "python-keyring"
pkgver = "25.6.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    # TODO: add a global keyring provider dependency
    "python-jaraco.context",
    "python-jaraco.functools",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Store and access your passwords safely"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/keyring"
source = f"$(PYPI_SITE)/k/keyring/keyring-{pkgver}.tar.gz"
sha256 = "0b39998aa941431eb3d9b0d4b2460bc773b9df6fed7621c2dfb291a7e0187a66"


def post_install(self):
    self.install_license("LICENSE")
