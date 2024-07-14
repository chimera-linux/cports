pkgname = "python-ytmusicapi"
pkgver = "1.7.5"
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
sha256 = "b306c330bdf81888f01d9f62fea96bf19bdd521999536988e98dbf6be41009fe"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
