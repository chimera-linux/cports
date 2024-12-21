pkgname = "python-ytmusicapi"
pkgver = "1.9.0"
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
sha256 = "1f703ba5c9c09208cd124b9feb578d9ab39e558b6ca457ac037ea65e7db9b16c"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
