pkgname = "python-time-machine"
pkgver = "2.14.2"
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
sha256 = "d31729bb75a54b6be0c324be90a2fca074daefd5735d59fc24d1aad223ed07d1"


def post_install(self):
    self.install_license("LICENSE")
