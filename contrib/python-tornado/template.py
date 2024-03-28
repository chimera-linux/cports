pkgname = "python-tornado"
pkgver = "6.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-twisted"]
pkgdesc = "Web framework and asynchronous networking library"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "Apache-2.0"
url = "https://github.com/tornadoweb/tornado"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a01d87d875e6b348042b761ad469c4f821b6ee5988783040277b168192f3c859"


def do_check(self):
    self.do("python3", "-m", "tornado.test.runtests")
