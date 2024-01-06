pkgname = "python-meson"
pkgver = "0.15.0"
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
sha256 = "7c29eb0d17bb7813f5e5c89f5df5f56eda446e263b4d4a9f5f286548a0eb385f"


def post_install(self):
    self.install_license("LICENSE")
