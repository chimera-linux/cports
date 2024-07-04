pkgname = "python-ytmusicapi"
pkgver = "1.7.4"
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
sha256 = "a0abb52d5d652224a45eb172e4767e06eb49bec119bd7417b6b002c042c65454"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
