pkgname = "python-ytmusicapi"
pkgver = "1.9.1"
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
sha256 = "aade7da48e3d789f01947e4a701c3c29ccebfbf7b2b7a802b7ae9a8706c6bb54"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
