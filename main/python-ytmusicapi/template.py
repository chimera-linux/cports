pkgname = "python-ytmusicapi"
pkgver = "1.10.0"
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
sha256 = "7a5492b0b9b053f04e93e79fe0afaee46c2d47d9449450cbde4a5b079c7f5edf"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
