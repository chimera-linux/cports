pkgname = "python-qrcode"
pkgver = "8.2"
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
license = "BSD-3-Clause"
url = "https://github.com/lincolnloop/python-qrcode"
source = f"$(PYPI_SITE)/q/qrcode/qrcode-{pkgver}.tar.gz"
sha256 = "35c3f2a4172b33136ab9f6b3ef1c00260dd2f66f858f24d88418a015f446506c"


def post_install(self):
    self.install_license("LICENSE")
