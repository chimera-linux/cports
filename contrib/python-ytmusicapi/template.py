pkgname = "python-ytmusicapi"
pkgver = "1.7.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python-requests"]
checkdepends = ["python-pytest"] + depends
pkgdesc = "Python library for the Youtube Music API"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/sigma67/ytmusicapi"
source = f"$(PYPI_SITE)/y/ytmusicapi/ytmusicapi-{pkgver}.tar.gz"
sha256 = "63de01e6b8729cc3ee1a09650c9ec6e4932857b577dd90724ae2e770fbd88d50"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
