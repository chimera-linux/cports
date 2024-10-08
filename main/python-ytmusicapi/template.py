pkgname = "python-ytmusicapi"
pkgver = "1.8.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python-requests"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python library for the Youtube Music API"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/sigma67/ytmusicapi"
source = f"$(PYPI_SITE)/y/ytmusicapi/ytmusicapi-{pkgver}.tar.gz"
sha256 = "454facdf5907c32b77cb035f54c76d5a9d3fb0316933b1a1cecd06110ff85ecf"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
