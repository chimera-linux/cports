pkgname = "python-dnspython"
pkgver = "2.5.0"
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
sha256 = "a0034815a59ba9ae888946be7ccca8f7c157b286f8455b379c692efb51022a15"


def post_install(self):
    self.install_license("LICENSE")
