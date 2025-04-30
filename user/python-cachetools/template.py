pkgname = "python-cachetools"
pkgver = "5.5.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Extensible memoizing collections and decorators"
license = "MIT"
url = "https://github.com/tkem/cachetools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cf20ba6147ab761f4a74409097ce10c4b36aff209f5564ae6d61cc32362f5410"


def post_install(self):
    self.install_license("LICENSE")
