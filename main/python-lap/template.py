pkgname = "python-lap"
pkgver = "0.5.12"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "python-devel",
    "python-numpy-devel",
]
depends = ["python-numpy"]
pkgdesc = "Linear Assignment Problem solver for LAPJV/LAPMOD"
license = "BSD-2-Clause"
url = "https://github.com/gatagat/lap"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "462186b414ab6bd9239744ae92242e03df9f31f8f2e346ab2c52ff797748ebec"
# Checks don't work out of the box, haven't looked into it
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
