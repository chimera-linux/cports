pkgname = "python-dnspython"
pkgver = "2.6.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = ["python-pytest"]
pkgdesc = "DNS toolkit for Python"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "ISC"
url = "https://www.dnspython.org"
source = f"$(PYPI_SITE)/d/dnspython/dnspython-{pkgver}.tar.gz"
sha256 = "233f871ff384d84c33b2eaf4358ffe7f8927eae3b257ad8467f9bdba7e7ac6bc"


def post_install(self):
    self.install_license("LICENSE")
