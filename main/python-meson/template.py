pkgname = "python-meson"
pkgver = "0.18.0"
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
sha256 = "6435a1e3f59f3e40579659aa3e5866034c2072ad38060bd4cfec93a5f2471b02"


def post_install(self):
    self.install_license("LICENSE")
