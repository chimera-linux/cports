pkgname = "python-ytmusicapi"
pkgver = "1.11.0"
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
sha256 = "2f7620a3ee1e216c1661ff316ce42a2d69d2067f855ea900f375baf274c4799d"
# like all tests need net
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
