pkgname = "python-zstandard"
pkgver = "0.25.0"
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
pkgdesc = "Python bindings to the Zstandard compression library"
license = "BSD-3-Clause"
url = "https://github.com/indygreg/python-zstandard"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "851846ffe25681f7936ab2fd89130acf62b214a77b8c54e4319824f3510ab395"
# tests fail to find internal modules due to cwd
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
