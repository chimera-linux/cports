pkgname = "python-pyrfc3339"
pkgver = "1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pytz"]
pkgdesc = "Generate and parse RFC 3339 timestamps"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/kurtraschke/pyRFC3339"
source = f"$(PYPI_SITE)/p/pyRFC3339/pyRFC3339-{pkgver}.tar.gz"
sha256 = "81b8cbe1519cdb79bed04910dd6fa4e181faf8c88dff1e1b987b5f7ab23a5b1a"
# tests require nose
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
