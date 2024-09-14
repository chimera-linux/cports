pkgname = "python-itsdangerous"
pkgver = "2.2.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = [
    "python-freezegun",
    "python-pytest",
]
pkgdesc = "Python3 helper to pass trusted data to untrusted environments"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "BSD-3-Clause"
url = "https://github.com/pallets/itsdangerous"
source = f"$(PYPI_SITE)/i/itsdangerous/itsdangerous-{pkgver}.tar.gz"
sha256 = "e0050c0b7da1eea53ffaf149c0cfbb5c6e2e2b69c4bef22c81fa6eb73e5f6173"


def post_install(self):
    self.install_license("LICENSE.txt")
