pkgname = "python-zipfile-zstd"
pkgver = "0.0.4"
pkgrel = 0
build_style = "python_pep517"
make_build_args = ["--skip-dependency-check"]
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Patched zipfile module to enable Zstandard support"
license = "MIT"
url = "https://github.com/taisei-project/python-zipfile-zstd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f7bce303002b9f1365b24feb472c3fde218a1de4cc2d934837e6f8a6df823481"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
