pkgname = "python-meson"
pkgver = "0.16.0"
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
sha256 = "1f464e7a1e15971b70c8208d537fd0193b33c345aac5887af2806e55426ca571"


def post_install(self):
    self.install_license("LICENSE")
