pkgname = "python-tomlkit"
pkgver = "0.15.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = ["python-pytest", "python-pyyaml"]
depends = ["python"]
pkgdesc = "Style-preserving TOML python library"
license = "MIT"
url = "https://github.com/python-poetry/tomlkit"
source = f"$(PYPI_SITE)/t/tomlkit/tomlkit-{pkgver}.tar.gz"
sha256 = "e25bbf38843005246210a12982776f27f99cb9be67160e14434d0c0d21ee1e97"


def post_install(self):
    self.install_license("LICENSE")
