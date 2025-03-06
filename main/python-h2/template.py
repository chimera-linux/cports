pkgname = "python-h2"
pkgver = "4.2.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-hpack", "python-hyperframe"]
checkdepends = ["python-pytest", "python-hypothesis", *depends]
pkgdesc = "Python implementation of HTTP/2 state machine"
license = "MIT"
url = "https://github.com/python-hyper/h2"
source = f"$(PYPI_SITE)/h/h2/h2-{pkgver}.tar.gz"
sha256 = "c8a52129695e88b1a0578d8d2cc6842bbd79128ac685463b887ee278126ad01f"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
