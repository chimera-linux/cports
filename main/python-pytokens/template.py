pkgname = "python-pytokens"
pkgver = "0.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-mypy",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Python tokenizer"
license = "MIT"
url = "https://github.com/tusharsadhwani/pytokens"
source = f"$(PYPI_SITE)/p/pytokens/pytokens-{pkgver}.tar.gz"
sha256 = "292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
