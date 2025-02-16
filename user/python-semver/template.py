pkgname = "python-semver"
pkgver = "3.0.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python package to work with Semantic Versioning"
maintainer = "Julie Koubova <julie@koubova.net>"
license = "BSD-3-Clause"
url = "https://github.com/python-semver/python-semver"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9bcf622c80e2acabb8cf47c367adbea5ea782c882766ae56be0f5e6982176704"


def post_install(self):
    self.install_license("LICENSE.txt")
