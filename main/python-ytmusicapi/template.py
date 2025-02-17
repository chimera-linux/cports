pkgname = "python-ytmusicapi"
pkgver = "1.10.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/sigma67/ytmusicapi"
source = f"$(PYPI_SITE)/y/ytmusicapi/ytmusicapi-{pkgver}.tar.gz"
sha256 = "812685451916e76bf47b96f61ef5d4f4db408ea154a44d0779757539f62d69f9"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
