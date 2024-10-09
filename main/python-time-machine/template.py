pkgname = "python-time-machine"
pkgver = "2.16.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
]
depends = ["python-dateutil"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python library for mocking the current time"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/adamchainz/time-machine"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d2ed8ebef04133d69bce09114bbf66be0d404d725597874a644318af6e0b3e28"


def post_install(self):
    self.install_license("LICENSE")
