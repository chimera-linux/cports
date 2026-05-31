pkgname = "python-tomlkit"
pkgver = "0.15.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-poetry-core"]
checkdepends = ["python-pytest", "python-pyyaml"]
depends = ["python"]
pkgdesc = "Style-preserving TOML python library"
license = "MIT"
url = "https://github.com/sdispatcher/tomlkit"
source = f"$(PYPI_SITE)/t/tomlkit/tomlkit-{pkgver}.tar.gz"
sha256 = "7d1a9ecba3086638211b13814ea79c90dd54dd11993564376f3aa92271f5c7a3"


def post_install(self):
    self.install_license("LICENSE")
