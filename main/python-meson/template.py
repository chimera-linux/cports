pkgname = "python-meson"
pkgver = "0.19.0"
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
license = "MIT"
url = "https://meson-python.readthedocs.io/en/latest/index.html"
source = f"https://github.com/mesonbuild/meson-python/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2d3efafb7e85e93d766a1ae46a53aec97fc4c97bdb07c341f803a32be10b29e9"


def post_install(self):
    self.install_license("LICENSE")
