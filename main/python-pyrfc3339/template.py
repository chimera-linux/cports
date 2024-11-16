pkgname = "python-pyrfc3339"
pkgver = "2.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Generate and parse RFC 3339 timestamps"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/kurtraschke/pyRFC3339"
# pypi has no tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b608e002080bf3cad923d1c1c74078954b383ba509adbf05bee1d2915fd5b43a"
# tests require nose
# options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
