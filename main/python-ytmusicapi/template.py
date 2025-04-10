pkgname = "python-ytmusicapi"
pkgver = "1.10.3"
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
license = "MIT"
url = "https://github.com/sigma67/ytmusicapi"
source = f"$(PYPI_SITE)/y/ytmusicapi/ytmusicapi-{pkgver}.tar.gz"
sha256 = "7235361ac9d5958d49a29f586eec55b1c83e90f7b063361e8a206e1cf4f76216"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
