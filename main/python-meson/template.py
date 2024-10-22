pkgname = "python-meson"
pkgver = "0.17.0"
pkgrel = 0
build_style = "python_pep517"
# needs to be in git
make_check_args = ["-k", "not test_reproducible"]
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
sha256 = "1e287ae4bbe9fb6a07dd695d4fe2d0611e3090c55b4a46536b4c57b7056f3690"


def post_install(self):
    self.install_license("LICENSE")
