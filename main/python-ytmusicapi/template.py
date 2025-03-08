pkgname = "python-ytmusicapi"
pkgver = "1.10.2"
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
sha256 = "8fb4e63dcedd753aa0d755d7b1891df75e720e6ee9753d0e57a4dc015e411bf1"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
