pkgname = "python-time-machine"
pkgver = "2.14.1"
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
sha256 = "a57bfadf961318fca2ba840d15116176e253aa8689d88c830480b46f0ea5dcdf"


def post_install(self):
    self.install_license("LICENSE")
