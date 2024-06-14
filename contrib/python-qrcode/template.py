pkgname = "python-qrcode"
pkgver = "7.4.2"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["--ignore=qrcode/tests/test_release.py"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pypng"]
checkdepends = depends + ["python-pytest"]
pkgdesc = "Python QR code image generator"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/lincolnloop/python-qrcode"
source = f"$(PYPI_SITE)/q/qrcode/qrcode-{pkgver}.tar.gz"
sha256 = "9dd969454827e127dbd93696b20747239e6d540e082937c90f14ac95b30f5845"


def post_install(self):
    self.install_license("LICENSE")
