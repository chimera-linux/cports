pkgname = "python-publicsuffix2"
pkgver = "2.20191221"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-requests",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Get a public suffix for a domain name using PSL"
license = "MIT"
url = "https://github.com/nexB/python-publicsuffix2"
source = f"$(PYPI_SITE)/p/publicsuffix2/publicsuffix2-{pkgver}.tar.gz"
sha256 = "00f8cc31aa8d0d5592a5ced19cccba7de428ebca985db26ac852d920ddd6fe7b"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("publicsuffix2.LICENSE")
