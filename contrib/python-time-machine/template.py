pkgname = "python-time-machine"
pkgver = "2.14.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-dateutil"]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Python library for mocking the current time"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/adamchainz/time-machine"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "96d4d0d9af39004f74b705650bd5079c9208ba2c94428621863982e914ed0884"


def post_install(self):
    self.install_license("LICENSE")
