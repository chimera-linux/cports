pkgname = "python-meson"
pkgver = "0.17.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "meson",
    "patchelf",
    "python-build",
    "python-installer",
    "python-pyproject-metadata",
    "python-wheel",
]
depends = ["meson", "patchelf", "python-pyproject-metadata"]
checkdepends = [
    "git",
    "python-cython",
    "python-devel",
    "python-pytest",
    "python-pytest-mock",
]
pkgdesc = "Meson PEP 517 Python build backend"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://meson-python.readthedocs.io/en/latest/index.html"
source = f"https://github.com/mesonbuild/meson-python/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d533356468000e6f126215dded75dd9b07c7cbe14ca9f78c51791d4172b6e4a5"


def post_install(self):
    self.install_license("LICENSE")
