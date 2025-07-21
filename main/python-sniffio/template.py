pkgname = "python-sniffio"
pkgver = "1.3.1"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Runtime async library detection for Python"
license = "Apache-2.0 AND MIT"
url = "https://github.com/python-trio/sniffio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eaaf93c6b263537535e4df0e070586e2ccae467153bb5eb7d588b8af98f24504"


def post_install(self):
    self.install_license("LICENSE.MIT")
