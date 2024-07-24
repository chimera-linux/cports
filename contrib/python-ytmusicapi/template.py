pkgname = "python-ytmusicapi"
pkgver = "1.8.0"
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
sha256 = "8b2bec6a4615f5144fc5f2daaeaab3cd059b602d916f323ef72b7d71b1e21f95"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
