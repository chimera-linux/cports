pkgname = "python-tblib"
pkgver = "3.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = [
    "python-pytest",
    "python-twisted",
]
pkgdesc = "Traceback serialization library"
license = "BSD-2-Clause"
url = "https://github.com/ionelmc/python-tblib"
source = f"$(PYPI_SITE)/t/tblib/tblib-{pkgver}.tar.gz"
sha256 = "93622790a0a29e04f0346458face1e144dc4d32f493714c6c3dff82a4adb77e6"


def post_install(self):
    self.install_license("LICENSE")
