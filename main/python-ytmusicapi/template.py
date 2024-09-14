pkgname = "python-ytmusicapi"
pkgver = "1.8.1"
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
sha256 = "1bd4a85f81efe824a4eaec26502b9d27887792f590d80bbdf3c9c5943ec5fd6e"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
