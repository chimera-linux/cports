pkgname = "python-time-machine"
pkgver = "2.15.0"
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
sha256 = "1b8d9e36813cbaee65e554f0c104e09ac9cb2a54ac641e5dadd969550496f8ed"


def post_install(self):
    self.install_license("LICENSE")
