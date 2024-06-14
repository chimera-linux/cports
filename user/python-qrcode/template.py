pkgname = "python-qrcode"
pkgver = "8.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--ignore=qrcode/tests/test_release.py"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-pypng"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python QR code image generator"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/lincolnloop/python-qrcode"
source = f"$(PYPI_SITE)/q/qrcode/qrcode-{pkgver}.tar.gz"
sha256 = "025ce2b150f7fe4296d116ee9bad455a6643ab4f6e7dce541613a4758cbce347"


def post_install(self):
    self.install_license("LICENSE")
